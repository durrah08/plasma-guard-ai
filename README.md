**PlasmaGuard AI**

Autonomous Compliance & Triage for Stablecoin Payments
PlasmaGuard AI is a multi-agent system designed to de-risk stablecoin payments. We use AI "Swarms" to detect financial crime (like structuring) in real-time on the Plasma L1.

🚀 Vision
The Plasma network's zero-fee USD₮ feature is a breakthrough for financial inclusion, but it creates a "Compliance Honeypot" for financial crimes. PlasmaGuard provides the necessary institutional security layer that monitors the network in real-time, performing "Agentic Triage" to de-risk high-throughput stablecoin movements.

🤖 AI Agent Architecture
Our architecture utilizes a LangGraph-driven Agent Swarm to perform distributed risk triage:

- Analyst Agent: Monitors transaction patterns using KNN (K-Nearest Neighbors) models to detect behavioral deviations and "Peel Chain" patterns.

- Auditor Agent: Verifies global compliance (MiCA/FATF) by mapping geographic risk weights and sanctions lists.

- Guardrail Layer: Uses Guardrails AI to ensure agents never authorize unsafe transfers and prevents PII leakage.

🛠️ Tech Stack
- Blockchain: Plasma L1 (USD₮₀) - Live connection via Web3.py to the Plasma Testnet RPC.

- AI Framework: LangGraph / Python.

- Safety: Guardrails AI / ZK-Proofs.

- Smart Contract: Solidity-based "Digital Lock" (PlasmaGuard.sol).

🧠 How it Works
1. The Observer (Web3.py & Live RPC)
The system is live-connected to the Plasma Testnet RPC. It utilizes Web3.py to synchronize with the blockchain, providing a real-time pulse of network activity and block height on the dashboard.

2. The Final Arbiter (Constrained Smart Contract)
The PlasmaGuard.sol smart contract acts as the "Digital Lock":

Programmable Compliance: Hard-coded thresholds automatically divert suspicious funds to Escrow.

Autonomous Verification: The AI Swarm turns the "Key" by calling setVerified() only after a user passes the risk-weighted identity check.

3. The Command Center (Streamlit Dashboard)
A professional-grade financial dashboard featuring:

Live Transaction Triage: Real-time visualization of agents "talking" as they analyze incoming blocks.

Human-in-the-Loop (HITL): A manual override interface for lead compliance officers to verify or dismiss AI flags.

🏁 Getting Started
Prerequisites
Python 3.10+

Plasma Testnet XPL (from a faucet) for contract interaction.

Installation
Clone the Repo:

Bash

git clone https://github.com/your-repo/plasmaguard-ai.git
cd plasmaguard-ai

Install Dependencies:

Bash

pip install -r requirements.txt

Run the App:

Bash

streamlit run app.py
