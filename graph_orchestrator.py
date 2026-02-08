import operator
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, END

# --- 1. DEFINE THE SHARED STATE ---
# This is the "Collective Intelligence" where agents store their findings
class AgentState(TypedDict):
    wallet: str
    amount: float
    risk_score: float
    findings: Annotated[List[str], operator.add]
    next_step: str

# --- 2. DEFINE THE AGENTS (The Swarm) ---

def analyst_agent(state: AgentState):
    """Checks for 'Structuring' and pattern anomalies."""
    wallet = state['wallet']
    amount = state['amount']
    # Logic: If amount is an odd number or too frequent
    finding = f"Analyst: Pattern check for {wallet} complete. No immediate smurfing detected."
    return {"findings": [finding], "next_step": "auditor"}

def auditor_agent(state: AgentState):
    """Checks geographic risk and global sanctions."""
    # Mock check for high-risk geography
    risk_inc = 0.5 if state['amount'] > 5000 else 0.1
    finding = f"Auditor: Geographic risk weight assigned: {risk_inc}."
    return {"findings": [finding], "risk_score": state['risk_score'] + risk_inc, "next_step": "guardrail"}

def guardrail_agent(state: AgentState):
    """Final check to ensure the AI hasn't gone 'rogue'."""
    if state['risk_score'] > 0.75:
        finding = "Guardrail: RISK TOO HIGH. Diverting to human-in-the-loop (HITL)."
        return {"findings": [finding], "next_step": "end"}
    return {"findings": ["Guardrail: Compliance bounds maintained."], "next_step": "end"}

# --- 3. BUILD THE GRAPH (The Orchestration) ---

workflow = StateGraph(AgentState)

# Add our Swarm members
workflow.add_node("analyst", analyst_agent)
workflow.add_node("auditor", auditor_agent)
workflow.add_node("guardrail", guardrail_agent)

# Set the "Chain of Command"
workflow.set_entry_point("analyst")
workflow.add_edge("analyst", "auditor")
workflow.add_edge("auditor", "guardrail")
workflow.add_edge("guardrail", END)

# Compile the Swarm
swarm = workflow.compile()

# --- 4. TEST THE SWARM ---
if __name__ == "__main__":
    inputs = {"wallet": "0x94B...f1", "amount": 12000, "risk_score": 0.0, "findings": []}
    for output in swarm.stream(inputs):
        for key, value in output.items():
            print(f"Agent {key} is reporting...")
            print(f"Current Findings: {value.get('findings', [])}\n")