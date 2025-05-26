"""Groq reasoning agent for technical analysis."""

from langchain_core.messages import HumanMessage, SystemMessage
from src.agents.base_agent import BaseAgent
from src.workflow.state import AgentState
from src.models.model_factory import ModelFactory

class GroqReasoningAgent(BaseAgent):
    """Groq agent for technical reasoning and analysis."""
    
    def __init__(self):
        groq_model, _ = ModelFactory.get_models()
        super().__init__(groq_model)
    
    def process(self, state: AgentState) -> dict:
        """Process technical reasoning with Groq."""
        system_prompt = """You are a senior software architect with 15+ years of experience. Analyze the user's requirements and provide structured technical reasoning.

Focus on:
1. **Architecture Pattern Analysis** (max 200 words):
   - Evaluate different patterns (microservices, monolithic, serverless, event-driven)
   - Justify your recommended pattern with specific technical reasons
   - Consider scalability, maintainability, and team structure

2. **Technical Decision Framework** (max 150 words):
   - Key technology choices and trade-offs
   - Performance considerations
   - Development complexity assessment

3. **Infrastructure Planning** (max 150 words):
   - Compute, storage, and network requirements
   - Scaling strategies and bottleneck identification
   - Cloud vs on-premise considerations

4. **Risk Assessment** (max 100 words):
   - Technical risks and mitigation strategies
   - Implementation challenges

Be specific, technical, and focus on practical engineering decisions. Avoid generic advice."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=state["messages"][-1].content)
        ]
        
        response = self.model.invoke(messages)
        
        return {
            "groq_reasoning": response.content,
            "current_step": "groq_complete"
        }
