"""Application settings and configuration."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings."""
    
    # API Keys
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    
    # Model configurations
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    GEMINI_MODEL: str = "gemini-2.0-flash"
    
    # Temperature settings
    GROQ_TEMPERATURE: float = 0.1
    GEMINI_TEMPERATURE: float = 0.2
    
    # UI Configuration
    PAGE_TITLE: str = "System Architect Groq-Gemini Agent"
    PAGE_ICON: str = "🏗️"
    LAYOUT: str = "wide"
    
    # Analysis types
    ANALYSIS_TYPES: list = [
        "Real-time Event Processing",
        "Healthcare Data Platform",
        "Financial Trading Platform",
        "Multi-tenant SaaS",
        "Content Delivery Network",
        "Supply Chain Management",
        "IoT & Edge Computing",
        "AI/ML Model Serving",
        "E-commerce Platform",
        "Gaming & Multiplayer Systems",
        "Blockchain & DeFi Platform",
        "Video Streaming Platform"
    ]
    
    def validate_api_keys(self) -> bool:
        """Validate that required API keys are present."""
        return bool(self.GROQ_API_KEY and self.GOOGLE_API_KEY)

# Global settings instance
settings = Settings()
