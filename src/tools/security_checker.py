"""Security and compliance checking tool."""

import json
from langchain_core.tools import tool

@tool
def security_compliance_check(industry: str) -> str:
    """Check security and compliance requirements for specific industries."""
    compliance_map = {
        "healthcare": ["HIPAA", "HITECH", "FDA", "GDPR"],
        "finance": ["PCI-DSS", "SOX", "GDPR", "Basel III"],
        "ecommerce": ["PCI-DSS", "GDPR", "CCPA", "SOC2"],
        "government": ["FedRAMP", "FISMA", "NIST", "SOC2"],
        "general": ["GDPR", "SOC2", "ISO27001", "CCPA"]
    }
    return json.dumps(compliance_map.get(industry, compliance_map["general"]))
