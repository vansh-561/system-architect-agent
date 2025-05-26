"""Model factory for creating and managing AI models."""

import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings

class ModelFactory:
    """Factory class for creating AI models."""
    
    @staticmethod
    @st.cache_resource
    def create_groq_model() -> ChatGroq:
        """Create and cache Groq model."""
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.GROQ_MODEL,
            temperature=settings.GROQ_TEMPERATURE
        )
    
    @staticmethod
    @st.cache_resource
    def create_gemini_model() -> ChatGoogleGenerativeAI:
        """Create and cache Gemini model."""
        return ChatGoogleGenerativeAI(
            api_key=settings.GOOGLE_API_KEY,
            model=settings.GEMINI_MODEL,
            temperature=settings.GEMINI_TEMPERATURE
        )
    
    @classmethod
    def get_models(cls):
        """Get both models."""
        return cls.create_groq_model(), cls.create_gemini_model()
