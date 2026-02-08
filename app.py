import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from web3 import Web3
import time
import random

# --- 1. BLOCKCHAIN CONNECTION ---
# Connecting to the Plasma Testnet RPC you provided
PLASMA_RPC = "https://rpc-testnet.plasma.network"
w3 = Web3(Web3.HTTPProvider(PLASMA_RPC))

st.set_page_config(page_title="PlasmaGuard AI: Institutional Swarm", layout="wide")

# --- 2. THE CORE LOGIC (Structuring & Fincrime) ---
def analyze_fincrime(amount, geo_risk, history_count):
    """Refined Logic: Prevents zero-value false positives"""
    if amount <= 0:
        return "ℹ️ SYSTEM: No Value Transferred.", 0.0, "Non-Financial Event"
    
    # Structuring: Positive value under $1000 with high frequency
    if 0 < amount < 1000 and history_count > 3:
        return "🚩 CRIME: Structuring (Smurfing)", 0.88, "SAR Drafted"
    
    # Sanctions / Geographic Risk
    if geo_risk > 0.8:
        return "🚫 CRIME: Sanctions Evasion", 0.95, "Immediate Block"
    
    return "✅ CLEAR: Baseline Match", 0.15, "Approved"

# --- 3. FRONTEND STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; }
    .stMetric { border: 1px solid #00ff41; padding: 15px; border-radius: 10px; background-color: #1e2227; }
    [data-testid="stMetricValue"] { color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ PlasmaGuard AI: Autonomous Compliance Swarm")
st.caption("Powered by PlasmaBFT & 0x API")

# --- 4. LIVE NETWORK PULSE ---
try:
    current_block = w3.eth.block_number
    status = "Active"
except:
    current_block = "Offline"
    status = "Reconnecting..."

m1, m2, m3 = st.columns(3)
m1.metric("Live Plasma Block", current_block)
m2.metric("Network Status", status)
m3.metric("Swarm Health", "4 Nodes Operational")

st.divider()

# --- 5. TRIAGE DASHBOARD ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📡 Live Transaction Triage")
    
    # Automated Live Feed simulation
    mock_data = [
        {"Wallet": "0x71C...a2", "Amount": 850.0, "Asset": "USDT", "Geo_Risk": 0.1},
        {"Wallet": "0x94B...f1", "Amount": 125000.0, "Asset": "USDT", "Geo_Risk": 0.2},
        {"Wallet": "0x32A...e9", "Amount": 0.0, "Asset": "USDT", "Geo_Risk": 0.0},
        {"Wallet": "0xSan...z1", "Amount": 500.0, "Asset": "USDT", "Geo_Risk": 0.9}
    ]
    df = pd.DataFrame(mock_data)
    st.dataframe(df, width="stretch")

    selected_idx = st.selectbox("Select Transaction to Audit", df.index)
    selected_tx = df.iloc[selected_idx]

    if st.button("🚀 Execute Swarm Analysis"):
        with st.status("🛸 Orchestrating Agent Swarm...", expanded=True) as status:
            st.write("🕵️ **Analyst Agent:** Scanning for 'Peel Chain' & Structuring patterns...")
            time.sleep(0.8)
            st.write("🌊 **0x Agent:** Checking Slippage & Liquidity Risk...")
            time.sleep(0.8)
            st.write("⚖️ **Auditor Agent:** Pulling Global Sanctions via MCP...")
            time.sleep(0.5)
            status.update(label="Triage Complete", state="complete", expanded=False)

        # Run the refined logic
        label, score, action = analyze_fincrime(selected_tx['Amount'], 5, selected_tx['Geo_Risk'])
        
        if "🚩" in label or "🚫" in label:
            st.error(f"{label} | Action: {action}")
            st.info(f"**AI Narrative:** Transaction flagged due to behavioral deviation. Risk Score: {score}")
        elif "ℹ️" in label:
            st.warning(label)
        else:
            st.success(label)

with col_right:
    st.subheader("📊 Swarm Intelligence Metrics")
    # Risk Gauge
    # For the demo, let's dynamic the gauge based on the selection
    demo_score = 90 if selected_tx['Amount'] < 1000 and selected_tx['Amount'] > 0 else 15
    if selected_tx['Geo_Risk'] > 0.8: demo_score = 98

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = demo_score,
        title = {'text': "Risk Probability (%)"},
        gauge = {'bar': {'color': "#00ff41"}, 'steps': [{'range': [0, 70], 'color': "gray"}, {'range': [70, 100], 'color': "red"}]}
    ))
    fig.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(fig, width="stretch")

    st.markdown("### 👤 Human Override")
    if st.button("✅ Confirm AI Verdict"):
        st.toast("Feedback logged to KNN model.")
    if st.button("❌ Dismiss Flag"):
        st.toast("False positive reported. Swarm learning...")

st.divider()
st.caption("Institutional-grade stablecoin security for the Plasma L1 ecosystem.")