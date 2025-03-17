# 🧠 Ollama DeepSeek Interface

A Python-based interface for interacting with Ollama's API, specifically designed to work with the DeepSeek R1 8B model.

## 🔍 Overview

This project provides several Python scripts to interact with the Ollama API in different ways:
- 📝 Simple text generation
- 💬 Chat interface with streaming responses
- 🧵 Chat with conversation context/history

The project also includes a Dockerfile to set up Ollama with the DeepSeek-R1 8B model pre-loaded.

## ✅ Prerequisites

- 🐳 Docker (for container-based setup)
- 🐍 Python 3.6+
- 📦 `requests` library

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Docker Setup

Build and run the Docker container with the DeepSeek model:

```bash
# Build the Docker image
docker build -t ollama-deepseek .

# Run the container
docker run -d --name ollama-deepseek -p 11434:11434 ollama-deepseek
```

### 3. Verify Setup

Ensure the model is running properly:

```bash
# Check available models
docker exec -it ollama-deepseek ollama list

# Test with a simple curl request
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:8b",
  "prompt": "Explain what is debt in simple terms."
}' -H "Content-Type: application/json"
```

## 🛠️ Usage

### Simple Text Generation

For basic text generation:

```bash
python interactive.py
```

You'll be prompted to enter your query and optionally specify a different model.

### Chat Interface

For a chat-style interface (single query):

```bash
python chat.py
```

This allows you to specify a user message, an optional system prompt, and choose the model.

### Conversation with Context

For an interactive chat that maintains conversation history:

```bash
python chat-context.py
```

This script maintains the conversation context, allowing for more coherent multi-turn interactions. Type 'exit' to end the conversation.

## 📋 Script Details

### `interactive.py`

Simple text generation using the `/api/generate` endpoint. Streams tokens as they're generated.

### `chat.py`

Uses the `/api/chat` endpoint for a more chat-like interaction. Supports system prompts for setting the behavior of the model.

### `chat-context.py`

Extends the chat functionality by maintaining conversation history, allowing for contextual multi-turn conversations.

## 🐳 Docker Container Management

```bash
# View logs
docker logs ollama-deepseek

# Stop the container
docker stop ollama-deepseek

# Remove the container
docker rm ollama-deepseek
```

## ⚙️ Customization

You can easily modify these scripts to work with other Ollama models by changing the default model parameter.

## 🔧 Troubleshooting

- If you encounter connection issues, ensure the Ollama server is running and accessible at localhost:11434
- Check Docker logs for any errors: `docker logs ollama-deepseek`
- Verify that the model was downloaded successfully by running `ollama list` inside the container
