#!/bin/bash

echo "Setting up LangChain Agent Example..."
echo "======================================"

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required but not found."
    echo "Please install pip3 and try again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "Next steps:"
echo "1. Get your API keys:"
echo "   - Anthropic API key from: https://console.anthropic.com/"
echo "   - Tavily API key from: https://tavily.com/"
echo ""
echo "2. Set your environment variables:"
echo "   export ANTHROPIC_API_KEY='your_anthropic_key_here'"
echo "   export TAVILY_API_KEY='your_tavily_key_here'"
echo ""
echo "   Or copy .env.template to .env and fill in your keys:"
echo "   cp .env.template .env"
echo "   # Then edit .env with your actual API keys"
echo ""
echo "3. Run the example:"
echo "   source venv/bin/activate"
echo "   python langchain_agent_example.py"
echo ""