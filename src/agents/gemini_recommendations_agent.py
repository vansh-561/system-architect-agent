"""Gemini recommendations agent for implementation guidance."""

from langchain_core.messages import HumanMessage, SystemMessage
from src.agents.base_agent import BaseAgent
from src.workflow.state import AgentState
from src.models.model_factory import ModelFactory

class GeminiRecommendationsAgent(BaseAgent):
    """Gemini agent for detailed recommendations and roadmap."""
    
    def __init__(self):
        _, gemini_model = ModelFactory.get_models()
        super().__init__(gemini_model)
    
    def process(self, state: AgentState) -> dict:
        """Process recommendations with Gemini."""
        system_prompt = """Based on the Groq technical analysis, provide comprehensive implementation guidance and detailed recommendations.

Structure your response with:

## 🏗️ **Detailed Architecture Specification** (max 250 words)
- Specific implementation details for the recommended architecture
- Component interactions and data flow
- Technology integration patterns

## 📋 **Implementation Roadmap** (max 200 words)
- **Phase 1**: Foundation setup (weeks 1-4)
- **Phase 2**: Core development (weeks 5-12)
- **Phase 3**: Integration & testing (weeks 13-16)
- **Phase 4**: Deployment & monitoring (weeks 17-20)

## 🔒 **Security & Compliance Strategy** (max 150 words)
- Security measures implementation
- Compliance requirements mapping
- Data protection strategies

## 💰 **Cost-Benefit Analysis** (max 150 words)
- Development costs breakdown
- Operational expenses estimation
- ROI projections and cost optimization

## ⚠️ **Risk Mitigation Plan** (max 100 words)
- Critical risks identification
- Mitigation strategies
- Contingency planning

Use specific technologies, frameworks, and tools. Include realistic timelines and resource estimates."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"""
            Original Requirements: {state['messages'][-1].content}
            
            Analysis Type: {state['analysis_type']}
            
            Groq Technical Analysis: {state['groq_reasoning']}
            
            Provide comprehensive implementation guidance based on this technical analysis.
            """)
        ]
        
        response = self.model.invoke(messages)
        
        return {
            "gemini_recommendations": response.content,
            "current_step": "gemini_complete"
        }
