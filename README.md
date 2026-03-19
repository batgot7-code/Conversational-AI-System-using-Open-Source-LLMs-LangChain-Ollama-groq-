# Conversational-AI-System-using-Open-Source-LLMs (LangChain-Ollama/groq)

This project is a lightweight, modular Conversational AI system built using open-source Large Language Models (LLMs). It leverages LangChain for orchestration and supports both local inference via Ollama and ultra-fast cloud inference via Groq.

The system is designed to be flexible, efficient, and developer-friendly, making it ideal for building chatbots, assistants, and AI-powered applications without relying on proprietary models.

✨ Features

💬 Natural Conversational Interface
Context-aware multi-turn conversations

🔗 LangChain Integration
Prompt management, memory handling, and chaining capabilities

⚡ Dual Inference Support

Ollama → Run LLMs locally (privacy-focused)

Groq → High-speed inference using LPU acceleration

🧠 Conversation Memory
Maintains chat history for better contextual responses

🔌 Modular Design
Easily plug in different LLMs (LLaMA, Mistral, Qwen, etc.)

🌐 Streamlit UI (Optional)
Simple and interactive frontend for real-time chatting

🛠️ Tech Stack

Python

LangChain

Ollama (local LLMs)

Groq API (fast inference)

Streamlit (UI)

📌 Use Cases

AI Chatbots

Personal Assistants

Customer Support Systems

LLM Experimentation Playground

Educational AI Tools

⚙️ How It Works

User input is captured via CLI or Streamlit UI

LangChain processes the prompt and manages context

Request is routed to:

Local LLM via Ollama OR

Groq-hosted model for fast responses

Response is generated and returned with conversation memory

🎯 Goals

Provide a fully open-source alternative to closed AI systems

Enable local + cloud hybrid LLM workflows

Make LLM-based app development simple and scalable
