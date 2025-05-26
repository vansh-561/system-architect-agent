"""Progress tracking component."""

import streamlit as st
import time

class ProgressTracker:
    """Progress tracker for agent workflow."""
    
    def __init__(self):
        self.progress_bar = None
        self.status_text = None
    
    def start_tracking(self):
        """Start progress tracking."""
        self.progress_bar = st.progress(0)
        self.status_text = st.empty()
    
    def update_progress(self, progress: int, status: str):
        """Update progress and status."""
        if self.progress_bar and self.status_text:
            self.status_text.text(status)
            self.progress_bar.progress(progress)
    
    def complete(self):
        """Complete progress tracking."""
        if self.progress_bar and self.status_text:
            self.status_text.text("✅ Analysis complete!")
            self.progress_bar.progress(100)
            time.sleep(1)
            self.progress_bar.empty()
            self.status_text.empty()
