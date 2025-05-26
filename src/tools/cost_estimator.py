"""Infrastructure cost estimation tool."""

import json
from langchain_core.tools import tool

@tool
def estimate_infrastructure_costs(architecture: str, scale: str) -> str:
    """Estimate infrastructure costs based on architecture and scale."""
    cost_estimates = {
        "small": {"compute": 500, "storage": 100, "network": 50, "monitoring": 25},
        "medium": {"compute": 2000, "storage": 500, "network": 200, "monitoring": 100},
        "large": {"compute": 10000, "storage": 2000, "network": 1000, "monitoring": 500},
        "enterprise": {"compute": 50000, "storage": 10000, "network": 5000, "monitoring": 2500}
    }
    return json.dumps(cost_estimates.get(scale, cost_estimates["medium"]))
