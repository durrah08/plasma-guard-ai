import time

# This simulates a "Swarm" agent checking for "Structuring" (smurfing)
class ComplianceAgent:
    def __init__(self, threshold_amount=1000, max_transactions=3):
        self.threshold_amount = threshold_amount
        self.max_transactions = max_transactions
        self.history = {}

    def check_transaction(self, wallet, amount):
        current_time = time.time()
        
        # 1. Check for "Structuring" (Many small payments)
        if wallet not in self.history:
            self.history[wallet] = []
        
        self.history[wallet].append({"amount": amount, "time": current_time})
        
        # Clean history (only look at the last 10 minutes)
        self.history[wallet] = [t for t in self.history[wallet] if current_time - t['time'] < 600]

        if len(self.history[wallet]) > self.max_transactions:
            return "🚩 FLAG: Potential Structuring (Too many small payments)"
        
        # 2. Check for High Value Risk
        if amount > self.threshold_amount:
            return "⚠️ HOLD: High Value (Requires ZK-Proof verification)"
        
        return "✅ CLEAR: Transaction Approved"

# --- TEST THE AGENT ---
agent = ComplianceAgent()
print(agent.check_transaction("0x123...abc", 100)) # Clear
print(agent.check_transaction("0x123...abc", 100)) # Clear
print(agent.check_transaction("0x123...abc", 100)) # Clear
print(agent.check_transaction("0x123...abc", 100)) # Flag!


def generate_sar_narrative(wallet, risk_score, reason):
    prompt = f"""
    [REGULATORY DRAFT - CONFIDENTIAL]
    Subject Wallet: {wallet}
    Detected Risk: {risk_score}
    Reason: {reason}
    
    NARRATIVE: On 2026-02-07, the PlasmaGuard Swarm identified a series of 
    rapid-fire USDT transfers. This activity is consistent with 'Structuring' 
    patterns intended to evade reporting thresholds. The wallet originates 
    from a High-Risk Jurisdiction. Recommend immediate SAR filing.
    """
    return prompt

    from web3 import Web3

# Connect to Plasma Testnet

plasma_url = "https://rpc-testnet.plasma.network" 
w3 = Web3(Web3.HTTPProvider(plasma_url))

def check_connection():
    if w3.is_connected():
        print(f"✅ Connected to Plasma Testnet. Current Block: {w3.eth.block_number}")
    else:
        print("❌ Connection failed.")

check_connection()