"""Sidebar component for configuration."""

import streamlit as st
from config.settings import settings

def render_sidebar():
    """Render the sidebar with configuration options."""
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        analysis_type = st.selectbox(
            "Analysis Type",
            settings.ANALYSIS_TYPES
        )
        
        st.markdown("### 🎯 **Model Roles**")
        st.info("""
        **🧠 Groq Llama 3.3 70B**: Deep technical reasoning and architecture analysis
        
        **⚡ Gemini 2.0 Flash**: Implementation roadmap and detailed recommendations
        """)
        
        st.markdown("### 💡 **Tips for Better Analysis**")
        st.success("""
        - Specify your **scale** (users, data volume)
        - Mention **budget constraints**
        - Include **compliance requirements**
        - Describe **existing systems** to integrate
        - State **performance expectations**
        """)
        
        return analysis_type
