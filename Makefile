.PHONY: install install-dev test coverage format lint type-check clean help

help:
	@echo "Available commands:"
	@echo "  make install      - Install package dependencies"
	@echo "  make install-dev  - Install package with dev dependencies"
	@echo "  make test         - Run tests"
	@echo "  make coverage     - Run tests with coverage report"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Lint code with flake8"
	@echo "  make type-check   - Type check code with mypy"
	@echo "  make clean        - Remove build artifacts and cache"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest

coverage:
	pytest --cov=chatgpt --cov-report=html --cov-report=term

format:
	black chatgpt/ tests/ examples/

lint:
	flake8 chatgpt/ tests/ examples/ --max-line-length=100

type-check:
	mypy chatgpt/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
