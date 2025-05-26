"""Chat interface component."""

import streamlit as st

def render_chat_history():
    """Render chat history."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    """Get user input from chat interface."""
    return st.chat_input("Describe your system architecture requirements...")

def add_message(role: str, content: str):
    """Add message to session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    st.session_state.messages.append({"role": role, "content": content})

def display_message(role: str, content: str):
    """Display a message in the chat interface."""
    with st.chat_message(role):
        st.markdown(content)
