from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chatgpt-client",
    version="1.0.0",
    author="ChatGPT Client Team",
    description="A Python client for interacting with OpenAI's ChatGPT API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.12.0",
        "python-dotenv>=1.0.0",
    ],
)
