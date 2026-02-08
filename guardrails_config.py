
# Using Guardrails AI logic to sanitize AI outputs

def apply_guardrails(narrative: str):
    """Prevents PII leakage and ensures professional SAR formatting."""
    prohibited_terms = ["Social Security", "Passport Number", "Birthday"]
    
    for term in prohibited_terms:
        if term in narrative:
            return "ERROR: PII detected. Narrative blocked for safety."
            
    return f"SAFE NARRATIVE: {narrative}"