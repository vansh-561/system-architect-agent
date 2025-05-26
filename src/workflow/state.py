"""State management for the agent workflow."""

from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """State definition for the agent workflow."""
    messages: Annotated[list, add_messages]
    analysis_type: str
    groq_reasoning: str
    gemini_recommendations: str
    current_step: str
