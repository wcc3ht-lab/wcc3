# Contributing to ChatGPT Client

Thank you for your interest in contributing to the ChatGPT Client project!

## Development Setup

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

## Running Tests

```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=chatgpt --cov-report=html
```

## Code Style

This project uses:
- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

Before submitting a PR, please run:

```bash
black chatgpt/ tests/ examples/
flake8 chatgpt/ tests/ examples/
mypy chatgpt/
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Run code formatters and linters
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to your branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## Reporting Bugs

Please use the GitHub issue tracker to report bugs. Include:
- Python version
- Library version
- Minimal code to reproduce the issue
- Error messages and stack traces

## Feature Requests

Feature requests are welcome! Please open an issue describing:
- The problem you're trying to solve
- Your proposed solution
- Any alternative solutions you've considered

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
