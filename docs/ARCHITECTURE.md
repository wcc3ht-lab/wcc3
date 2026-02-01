# Architecture

## Project Structure

```
chatgpt-client/
├── chatgpt/              # Main package
│   ├── __init__.py      # Package initialization
│   ├── client.py        # ChatGPT client implementation
│   ├── cli.py           # Command-line interface
│   └── __main__.py      # Entry point for CLI
├── tests/               # Test suite
│   ├── __init__.py
│   └── test_client.py   # Client tests
├── examples/            # Usage examples
│   └── basic_usage.py   # Basic usage demonstration
├── docs/                # Documentation
│   └── ARCHITECTURE.md  # This file
└── ...                  # Configuration files

```

## Components

### Client (`chatgpt/client.py`)

The `ChatGPT` class is the core component that wraps the OpenAI API.

**Key Features:**
- API key management (environment variable or direct)
- Model selection (GPT-3.5-turbo, GPT-4, etc.)
- Conversation history tracking
- Streaming support
- Error handling

**Methods:**
- `chat()`: Send a message and receive a complete response
- `stream_chat()`: Send a message and receive a streaming response
- `reset_conversation()`: Clear conversation history
- `get_conversation_history()`: Get current conversation history
- `set_model()`: Change the model being used

### CLI (`chatgpt/cli.py`)

Command-line interface for interacting with ChatGPT.

**Modes:**
- Interactive mode: Continuous conversation
- Single query mode: One-off questions
- Streaming mode: Real-time response display

**Arguments:**
- `--query, -q`: Single query to send
- `--model, -m`: Model to use
- `--temperature, -t`: Temperature setting
- `--stream, -s`: Enable streaming

### Tests (`tests/`)

Comprehensive test suite using pytest.

**Test Coverage:**
- Initialization with/without API key
- Chat functionality
- System prompts
- Conversation history management
- Model switching
- Error handling
- Streaming responses

## Design Patterns

### Dependency Injection

The API key can be provided via constructor or environment variable, making the code flexible and testable.

### Conversation State Management

The client maintains conversation history internally, allowing for contextual conversations without manual state management.

### Iterator Pattern

Streaming responses use Python generators for efficient memory usage and real-time display.

## Error Handling

- API key validation on initialization
- Exception handling for API errors
- Rollback of conversation history on failed requests

## Future Enhancements

Potential areas for expansion:

1. **Function Calling**: Support for OpenAI function calling
2. **Token Counting**: Track and limit token usage
3. **Retry Logic**: Automatic retries with exponential backoff
4. **Rate Limiting**: Built-in rate limiting
5. **Async Support**: Async/await for concurrent requests
6. **Response Caching**: Cache responses to save API calls
7. **Multi-turn Templates**: Predefined conversation templates
8. **Image Support**: Integration with DALL-E or GPT-4 Vision
