"""Helper utilities for the application."""

import json
from typing import Dict, Any

def format_json_response(data: Dict[str, Any]) -> str:
    """Format JSON data for display."""
    return json.dumps(data, indent=2)

def validate_analysis_type(analysis_type: str, valid_types: list) -> bool:
    """Validate analysis type."""
    return analysis_type in valid_types

def generate_thread_id() -> str:
    """Generate a unique thread ID."""
    import time
    return f"arch_analysis_{int(time.time())}"
