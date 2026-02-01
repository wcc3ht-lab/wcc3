import os
from chatgpt import ChatGPT

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Please set OPENAI_API_KEY environment variable")
        return
    
    print("Example 1: Simple conversation")
    print("-" * 50)
    client = ChatGPT(api_key=api_key)
    
    response = client.chat("Hello! What's the weather like today?")
    print(f"Assistant: {response}\n")
    
    response = client.chat("Tell me a short joke")
    print(f"Assistant: {response}\n")
    
    print("\nExample 2: Using system prompt")
    print("-" * 50)
    client = ChatGPT(api_key=api_key)
    
    response = client.chat(
        "What is 2 + 2?",
        system_prompt="You are a helpful math tutor. Always explain your reasoning."
    )
    print(f"Assistant: {response}\n")
    
    print("\nExample 3: Using GPT-4")
    print("-" * 50)
    client = ChatGPT(api_key=api_key, model="gpt-4")
    
    response = client.chat("Explain quantum entanglement in simple terms")
    print(f"Assistant: {response}\n")
    
    print("\nExample 4: Streaming response")
    print("-" * 50)
    client = ChatGPT(api_key=api_key)
    
    print("Assistant: ", end="", flush=True)
    for chunk in client.stream_chat("Write a haiku about coding"):
        print(chunk, end="", flush=True)
    print("\n")
    
    print("\nExample 5: Resetting conversation")
    print("-" * 50)
    client = ChatGPT(api_key=api_key)
    
    client.chat("My name is Alice")
    response = client.chat("What is my name?")
    print(f"Before reset - Assistant: {response}")
    
    client.reset_conversation()
    response = client.chat("What is my name?")
    print(f"After reset - Assistant: {response}\n")


if __name__ == "__main__":
    main()
