#!/usr/bin/env python3
"""
LangChain Agent Example
A conversational agent that can search the web and remember context
"""

import os
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

def check_environment_variables():
    """Check if required environment variables are set"""
    required_vars = ["ANTHROPIC_API_KEY", "TAVILY_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease set these environment variables before running the script.")
        print("You can set them by running:")
        for var in missing_vars:
            print(f"  export {var}='your_api_key_here'")
        return False
    
    return True

def create_agent():
    """Create and configure the LangChain agent"""
    try:
        # Create memory for conversation history
        memory = MemorySaver()
        
        # Initialize the chat model (Claude 3.5 Sonnet)
        model = init_chat_model("anthropic:claude-3-5-sonnet-latest")
        
        # Create the search tool
        search = TavilySearch(max_results=2)
        tools = [search]
        
        # Create the agent with tools and memory
        agent_executor = create_react_agent(model, tools, checkpointer=memory)
        
        return agent_executor
        
    except Exception as e:
        print(f"Error creating agent: {e}")
        return None

def run_conversation_example():
    """Run the example conversation from the user's request"""
    
    # Check environment variables
    if not check_environment_variables():
        return
    
    # Create the agent
    agent_executor = create_agent()
    if not agent_executor:
        return
    
    # Configuration for conversation thread
    config = {"configurable": {"thread_id": "abc123"}}
    
    print("=" * 60)
    print("LangChain Agent Conversation Example")
    print("=" * 60)
    
    try:
        # First message: Introduction
        print("\n1. First interaction - Bob introduces himself:")
        print("-" * 40)
        
        input_message = {
            "role": "user",
            "content": "Hi, I'm Bob and I live in SF.",
        }
        
        for step in agent_executor.stream(
            {"messages": [input_message]}, config, stream_mode="values"
        ):
            step["messages"][-1].pretty_print()
        
        print("\n" + "=" * 60)
        
        # Second message: Weather query
        print("\n2. Second interaction - Bob asks about weather:")
        print("-" * 40)
        
        input_message = {
            "role": "user",
            "content": "What's the weather where I live?",
        }
        
        for step in agent_executor.stream(
            {"messages": [input_message]}, config, stream_mode="values"
        ):
            step["messages"][-1].pretty_print()
        
        print("\n" + "=" * 60)
        print("Conversation completed successfully!")
        print("The agent remembered that Bob lives in SF and searched for SF weather.")
        
    except Exception as e:
        print(f"Error during conversation: {e}")
        print("Make sure your API keys are correctly set and you have internet access.")

def interactive_mode():
    """Run the agent in interactive mode for custom conversations"""
    
    # Check environment variables
    if not check_environment_variables():
        return
    
    # Create the agent
    agent_executor = create_agent()
    if not agent_executor:
        return
    
    # Configuration for conversation thread
    config = {"configurable": {"thread_id": "interactive_session"}}
    
    print("=" * 60)
    print("Interactive LangChain Agent")
    print("=" * 60)
    print("Type 'exit' or 'quit' to end the conversation")
    print("The agent can search the web and remembers our conversation context")
    print("-" * 60)
    
    try:
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            input_message = {
                "role": "user",
                "content": user_input,
            }
            
            print("\nAgent:")
            for step in agent_executor.stream(
                {"messages": [input_message]}, config, stream_mode="values"
            ):
                step["messages"][-1].pretty_print()
                
    except KeyboardInterrupt:
        print("\n\nConversation interrupted. Goodbye!")
    except Exception as e:
        print(f"Error during conversation: {e}")

def main():
    """Main function to run the example"""
    print("Choose an option:")
    print("1. Run the original example conversation")
    print("2. Interactive mode (chat with the agent)")
    
    try:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            run_conversation_example()
        elif choice == "2":
            interactive_mode()
        else:
            print("Invalid choice. Please run the script again and choose 1 or 2.")
            
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()