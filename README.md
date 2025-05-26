# System Architect Agent

Expert software architecture planning and analysis agent using Groq Llama 3.3 70B and Google Gemini 2.0 Flash models.

## Features

- **Dual AI Model Architecture**: Groq for technical reasoning, Gemini for implementation guidance
- **Comprehensive Analysis**: Architecture patterns, cost estimation, security compliance
- **Interactive UI**: Streamlit-based web interface
- **Modular Design**: Clean separation of concerns with extensible architecture

## Installation

1. Install Poetry (if not already installed):
curl -sSL https://install.python-poetry.org | python3 -

text

2. Clone and setup:
git clone <system-architect-agent>
cd system-architect-agent
poetry install

text

3. Configure environment:
cp .env.example .env

Edit .env with your API keys
text

4. Run the application:
poetry run python main.py

text

## API Keys Required

- **Groq API Key**: Get from [console.groq.com](https://console.groq.com)
- **Google AI API Key**: Get from [ai.google.dev](https://ai.google.dev)

## Usage

1. Start the application
2. Select your analysis type from the sidebar
3. Describe your system architecture requirements
4. Get comprehensive analysis and recommendations
5. Download the report for future reference

## Project Structure

- `config/`: Application configuration
- `src/agents/`: AI agent implementations
- `src/tools/`: Analysis tools
- `src/workflow/`: LangGraph workflow definition
- `ui/`: Streamlit user interface components
Installation Commands
bash
# Initialize Poetry project
poetry init

# Install dependencies
poetry install

# Create .env file
cp .env.example .env

# Run the application
poetry run streamlit run main.py
