# ChatGPT API Client

A Python client for interacting with OpenAI's ChatGPT API.

## Features

- Simple and intuitive API wrapper
- Support for multiple models (GPT-4, GPT-3.5-turbo)
- Streaming responses
- Conversation history management
- Error handling and retries
- Command-line interface

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

### As a Library

```python
from chatgpt import ChatGPT

# Initialize the client
client = ChatGPT(api_key="your-api-key")

# Send a message
response = client.chat("Hello, how are you?")
print(response)

# Continue the conversation
response = client.chat("Tell me a joke")
print(response)

# Use a different model
client = ChatGPT(model="gpt-4")
response = client.chat("Explain quantum computing")
print(response)
```

### Command Line Interface

```bash
# Start interactive chat
python -m chatgpt.cli

# Single query
python -m chatgpt.cli --query "What is the capital of France?"

# Use a specific model
python -m chatgpt.cli --model gpt-4
```

## API Reference

### ChatGPT Class

#### `__init__(api_key=None, model="gpt-3.5-turbo")`

Initialize a new ChatGPT client.

- `api_key` (str, optional): OpenAI API key. If not provided, reads from `OPENAI_API_KEY` environment variable.
- `model` (str): The model to use. Default is "gpt-3.5-turbo".

#### `chat(message, system_prompt=None, temperature=0.7, max_tokens=None)`

Send a message and get a response.

- `message` (str): The user message to send.
- `system_prompt` (str, optional): System prompt to set context.
- `temperature` (float): Controls randomness (0-2). Default is 0.7.
- `max_tokens` (int, optional): Maximum tokens in response.

Returns: `str` - The assistant's response.

#### `reset_conversation()`

Clear the conversation history.

## License

MIT
