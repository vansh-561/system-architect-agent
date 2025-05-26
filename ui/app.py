"""Main Streamlit application."""

import streamlit as st
import time
from langchain_core.messages import HumanMessage

from config.settings import settings
from src.workflow.graph import WorkflowGraph
from ui.components.sidebar import render_sidebar
from ui.components.chat_interface import (
    render_chat_history, 
    get_user_input, 
    add_message, 
    display_message
)
from ui.components.progress_tracker import ProgressTracker

def check_api_keys():
    """Check if API keys are configured."""
    if not settings.validate_api_keys():
        st.error("⚠️ Please set all required API keys in your .env file")
        st.code("""
# Create a .env file with:
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
        """)
        st.markdown("### 🔑 **Get Your API Keys:**")
        st.markdown("- **Groq**: [console.groq.com](https://console.groq.com)")
        st.markdown("- **Google AI**: [ai.google.dev](https://ai.google.dev)")
        return False
    return True

def initialize_workflow():
    """Initialize the workflow graph."""
    if "agent_graph" not in st.session_state:
        with st.spinner("🔧 Initializing agent workflow..."):
            st.session_state.agent_graph = WorkflowGraph()

def process_user_input(prompt: str, analysis_type: str):
    """Process user input through the agent workflow."""
    # Add user message
    add_message("user", prompt)
    display_message("user", prompt)
    
    # Process with agent
    with st.chat_message("assistant"):
        # Progress tracking
        tracker = ProgressTracker()
        tracker.start_tracking()
        
        try:
            tracker.update_progress(25, "🧠 Analyzing with Groq Llama 3.3 70B...")
            
            config = {"configurable": {"thread_id": f"arch_analysis_{int(time.time())}"}}
            
            initial_state = {
                "messages": [HumanMessage(content=f"Analysis Type: {analysis_type}\n\nRequirements: {prompt}")],
                "analysis_type": analysis_type,
                "groq_reasoning": "",
                "gemini_recommendations": "",
                "current_step": "start"
            }
            
            tracker.update_progress(75, "⚡ Generating recommendations with Gemini 2.0 Flash...")
            
            # Run the agent
            result = st.session_state.agent_graph.invoke(initial_state, config)
            
            tracker.complete()
            
            # Display the final response
            final_message = result["messages"][-1].content
            st.markdown(final_message)
            
            # Add to session state
            add_message("assistant", final_message)
            
            # Add download button for the report
            st.download_button(
                label="📥 Download Report (.txt)",
                data=final_message,
                file_name="architecture_report.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"❌ Error during analysis: {str(e)}")
            st.info("Please check your API keys and try again.")

def main():
    """Main application function."""
    st.set_page_config(
        page_title=settings.PAGE_TITLE,
        page_icon=settings.PAGE_ICON,
        layout=settings.LAYOUT
    )
    
    st.title(f"{settings.PAGE_ICON} {settings.PAGE_TITLE}")
    st.markdown("*Expert software architecture analysis using **Groq Llama 3.3 70B** and **Google Gemini 2.0 Flash***")
    
    # Check API keys
    if not check_api_keys():
        return
    
    # Initialize workflow
    initialize_workflow()
    
    # Render sidebar and get analysis type
    analysis_type = render_sidebar()
    
    # Render chat interface
    render_chat_history()
    
    # Handle user input
    if prompt := get_user_input():
        process_user_input(prompt, analysis_type)

if __name__ == "__main__":
    main()
