"""Architecture pattern analysis tool."""

import json
from langchain_core.tools import tool

@tool
def analyze_architecture_patterns(requirements: str) -> str:
    """Analyze and recommend architecture patterns based on requirements."""
    patterns = {
        "microservices": "Best for large, complex systems with multiple teams and independent scaling",
        "monolithic": "Suitable for small to medium applications with simple deployment needs",
        "serverless": "Ideal for event-driven, auto-scaling applications with variable workloads",
        "event_driven": "Perfect for real-time processing and loose coupling between components",
        "layered": "Good for traditional enterprise applications with clear separation of concerns"
    }
    return json.dumps(patterns)
