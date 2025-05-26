"""Base agent class for common functionality."""

from abc import ABC, abstractmethod
from src.workflow.state import AgentState

class BaseAgent(ABC):
    """Base class for all agents."""
    
    def __init__(self, model):
        self.model = model
    
    @abstractmethod
    def process(self, state: AgentState) -> dict:
        """Process the agent's task."""
        pass
