# LangChain Basics & Groq Streamlit Chatbot

A hands-on project exploring foundational LangChain Expression Language (LCEL) concepts, multi-step sequential chains, and a fully functional web-based chat application powered by Groq.

## Features
- **LangChain Basics Notebook (`langchainbasics.ipynb`)**: Demonstrates chat model wrappers, dynamic prompt templates, output parsers, and custom sequential pipelines.
- **Interactive Streamlit App (`qachatbot.py`)**: A production-ready chat interface featuring:
  - Secure sidebar API key configuration.
  - Dynamic model selection sliders (`openai/gpt-oss-20b`, `qwen/qwen3.8-27b`).
  - Stateful chat history management using Streamlit session state.
  - Real-time token streaming via LangChain runnables.
