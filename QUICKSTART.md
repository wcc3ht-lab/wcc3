# Quick Start Guide

Get up and running with ChatGPT Client in 5 minutes!

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd chatgpt-client

# Install dependencies
pip install -r requirements.txt
```

## Setup

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

2. Set up your environment:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Your First Chat

### Method 1: Interactive CLI

```bash
python -m chatgpt.cli
```

You'll enter an interactive chat session. Type your messages and press Enter.

Commands:
- Type your message and press Enter to chat
- Type `reset` to clear conversation history
- Type `exit` or `quit` to end the session

### Method 2: Single Query

```bash
python -m chatgpt.cli --query "What is Python?"
```

### Method 3: Python Code

Create a file `my_chat.py`:

```python
from chatgpt import ChatGPT
import os

# Initialize the client
client = ChatGPT(api_key=os.getenv("OPENAI_API_KEY"))

# Send a message
response = client.chat("Hello! Tell me a fun fact.")
print(response)

# Continue the conversation
response = client.chat("Tell me more about that.")
print(response)
```

Run it:
```bash
python my_chat.py
```

## Common Use Cases

### Use GPT-4

```bash
python -m chatgpt.cli --model gpt-4
```

Or in code:
```python
client = ChatGPT(model="gpt-4")
```

### Streaming Responses

```bash
python -m chatgpt.cli --stream --query "Write a short story"
```

Or in code:
```python
for chunk in client.stream_chat("Write a short story"):
    print(chunk, end="", flush=True)
```

### Set System Prompt

```python
response = client.chat(
    "What's 2+2?",
    system_prompt="You are a helpful math tutor."
)
```

### Adjust Creativity (Temperature)

```bash
# More creative (0-2, default 0.7)
python -m chatgpt.cli --temperature 1.2
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [examples/basic_usage.py](examples/basic_usage.py) for more examples
- Review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) to understand the design
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Troubleshooting

### "API key must be provided"
Make sure your `.env` file exists and contains `OPENAI_API_KEY=your-key`

### "Module not found"
Install dependencies: `pip install -r requirements.txt`

### Rate limit errors
You may need to wait or upgrade your OpenAI plan

## Help

```bash
python -m chatgpt.cli --help
```

Happy chatting! 🤖
