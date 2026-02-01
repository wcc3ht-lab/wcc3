import argparse
import os
import sys
from dotenv import load_dotenv
from .client import ChatGPT


def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="ChatGPT CLI")
    parser.add_argument(
        "--query",
        "-q",
        type=str,
        help="Single query to send to ChatGPT"
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default="gpt-3.5-turbo",
        help="Model to use (default: gpt-3.5-turbo)"
    )
    parser.add_argument(
        "--temperature",
        "-t",
        type=float,
        default=0.7,
        help="Temperature for response generation (default: 0.7)"
    )
    parser.add_argument(
        "--stream",
        "-s",
        action="store_true",
        help="Enable streaming responses"
    )
    
    args = parser.parse_args()
    
    try:
        client = ChatGPT(model=args.model)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    if args.query:
        try:
            if args.stream:
                print("Assistant: ", end="", flush=True)
                for chunk in client.stream_chat(
                    args.query,
                    temperature=args.temperature
                ):
                    print(chunk, end="", flush=True)
                print()
            else:
                response = client.chat(args.query, temperature=args.temperature)
                print(f"Assistant: {response}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("ChatGPT CLI - Interactive Mode")
        print(f"Model: {args.model}")
        print("Type 'exit' or 'quit' to end the conversation")
        print("Type 'reset' to clear conversation history")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["exit", "quit"]:
                    print("Goodbye!")
                    break
                
                if user_input.lower() == "reset":
                    client.reset_conversation()
                    print("Conversation history cleared.")
                    continue
                
                if args.stream:
                    print("Assistant: ", end="", flush=True)
                    for chunk in client.stream_chat(
                        user_input,
                        temperature=args.temperature
                    ):
                        print(chunk, end="", flush=True)
                    print()
                else:
                    response = client.chat(user_input, temperature=args.temperature)
                    print(f"Assistant: {response}")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
