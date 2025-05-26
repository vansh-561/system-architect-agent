"""LangGraph workflow definition."""

import time
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from src.workflow.state import AgentState
from src.agents.groq_reasoning_agent import GroqReasoningAgent
from src.agents.gemini_recommendations_agent import GeminiRecommendationsAgent
from src.tools.architecture_analyzer import analyze_architecture_patterns
from src.tools.cost_estimator import estimate_infrastructure_costs
from src.tools.security_checker import security_compliance_check
from src.tools.tech_stack_recommender import technology_stack_recommendations

class WorkflowGraph:
    """Main workflow graph for the system architect agent."""
    
    def __init__(self):
        self.groq_agent = GroqReasoningAgent()
        self.gemini_agent = GeminiRecommendationsAgent()
        self.graph = self._create_graph()
    
    def _groq_reasoning_node(self, state: AgentState) -> dict:
        """Groq reasoning node."""
        return self.groq_agent.process(state)
    
    def _gemini_recommendations_node(self, state: AgentState) -> dict:
        """Gemini recommendations node."""
        return self.gemini_agent.process(state)
    
    def _final_output_node(self, state: AgentState) -> dict:
        """Compile final comprehensive architecture report."""
        final_response = f"""
# 🏗️ System Architecture Analysis Report

## 🧠 Technical Analysis & Reasoning
*Powered by Groq Llama 3.3 70B*

{state['groq_reasoning']}

---

## 📋 Implementation Recommendations & Roadmap
*Powered by Google Gemini 2.0 Flash*

{state['gemini_recommendations']}

---

## 📊 **Analysis Summary**

**Analysis Type**: {state['analysis_type']}  
**Architecture Approach**: Dual-model technical analysis  
**Models Used**: Groq Llama 3.3 70B + Google Gemini 2.0 Flash  

*This analysis combines deep technical reasoning with practical implementation guidance to provide comprehensive architecture recommendations.*
"""
        
        return {
            "messages": [AIMessage(content=final_response)],
            "current_step": "complete"
        }
    
    def _create_graph(self):
        """Create the LangGraph workflow."""
        # Initialize tools
        tools = [
            analyze_architecture_patterns,
            estimate_infrastructure_costs,
            security_compliance_check,
            technology_stack_recommendations
        ]
        tool_node = ToolNode(tools)
        
        # Create the graph
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("groq_node", self._groq_reasoning_node)
        workflow.add_node("gemini_node", self._gemini_recommendations_node)
        workflow.add_node("tools", tool_node)
        workflow.add_node("final_output", self._final_output_node)
        
        # Define the flow
        workflow.add_edge(START, "groq_node")
        workflow.add_edge("groq_node", "gemini_node")
        workflow.add_edge("gemini_node", "final_output")
        workflow.add_edge("final_output", END)
        
        # Add memory
        memory = MemorySaver()
        
        return workflow.compile(checkpointer=memory)
    
    def invoke(self, initial_state: dict, config: dict):
        """Invoke the workflow."""
        return self.graph.invoke(initial_state, config)
