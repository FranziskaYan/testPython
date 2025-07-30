# LangChain Agent Example

A conversational AI agent built with LangChain that can search the web and maintain conversation context using memory.

## Features

- **Conversational Memory**: Remembers previous interactions within a conversation thread
- **Web Search**: Uses Tavily Search to find real-time information
- **Claude 3.5 Sonnet**: Powered by Anthropic's latest language model
- **Interactive Mode**: Chat with the agent in real-time
- **Example Mode**: Run the original Bob/SF weather example

## Quick Start

### 1. Run the Setup Script

```bash
./setup.sh
```

This will:
- Create a Python virtual environment
- Install all required dependencies
- Display next steps

### 2. Get API Keys

You'll need two API keys:

- **Anthropic API Key**: Get from [https://console.anthropic.com/](https://console.anthropic.com/)
- **Tavily API Key**: Get from [https://tavily.com/](https://tavily.com/)

### 3. Set Environment Variables

Option A - Export directly:
```bash
export ANTHROPIC_API_KEY='your_anthropic_key_here'
export TAVILY_API_KEY='your_tavily_key_here'
```

Option B - Use .env file:
```bash
cp .env.template .env
# Edit .env with your actual API keys
```

### 4. Run the Example

```bash
source venv/bin/activate
python langchain_agent_example.py
```

## Usage

When you run the script, you'll see two options:

1. **Run the original example conversation**: Reproduces the exact Bob/SF weather example
2. **Interactive mode**: Chat with the agent yourself

### Example Conversation

The original example demonstrates:
1. Bob introduces himself and mentions he lives in SF
2. Bob asks "What's the weather where I live?"
3. The agent remembers Bob lives in SF and searches for San Francisco weather

## Files

- `langchain_agent_example.py`: Main script with the agent implementation
- `requirements.txt`: Python dependencies
- `setup.sh`: Automated setup script
- `.env.template`: Template for environment variables
- `simple_example.py`: Original Python example (unrelated to LangChain)

## How It Works

1. **Memory**: Uses LangGraph's MemorySaver to maintain conversation context
2. **Model**: Initializes Claude 3.5 Sonnet via LangChain's chat model interface
3. **Tools**: Provides Tavily Search for real-time web information
4. **Agent**: Uses LangGraph's ReAct agent pattern to combine reasoning and actions

## Dependencies

- `langchain`: Core LangChain framework
- `langchain-anthropic`: Anthropic model integration
- `langchain-tavily`: Tavily search integration
- `langgraph`: Graph-based agent framework
- `tavily-python`: Tavily search API client

## Troubleshooting

- **Missing API keys**: The script will check and prompt for required environment variables
- **Import errors**: Make sure you've activated the virtual environment and installed dependencies
- **Network issues**: The agent requires internet access for web search functionality