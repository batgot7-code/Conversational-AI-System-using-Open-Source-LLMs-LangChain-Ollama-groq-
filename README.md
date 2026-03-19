# Conversational-AI-System-using-Open-Source-LLMs (LangChain-Ollama/groq)

<b>Conversational AI System using Open-Source LLMs </b>

(LangChain + Ollama / Groq)

This project is a lightweight, modular Conversational AI system built using open-source Large Language Models (LLMs). It leverages LangChain for orchestration and supports both local inference via Ollama and ultra-fast cloud inference via Groq.

The system is designed to be flexible, efficient, and developer-friendly, making it ideal for building chatbots, assistants, and AI-powered applications without relying on proprietary models.

<b>Features </b>

<b>Natural Conversational Interface </b>
Context-aware multi-turn conversations

<b>LangChain Integration </b>
Prompt management, memory handling, and chaining capabilities

<b>Dual Inference Support </b>

Ollama → Run LLMs locally (privacy-focused)

Groq → High-speed inference using LPU acceleration

<b>Conversation Memory </b>
Maintains chat history for better contextual responses

<b>Modular Design </b>
Easily plug in different LLMs (LLaMA, Mistral, Qwen, etc.)

<b>Streamlit UI (Optional) </b>
Simple and interactive frontend for real-time chatting

<b>Tech Stack </b>

Python

LangChain

Ollama (local LLMs)

Groq API (fast inference)

Streamlit (UI)

<b>Use Cases </b>

AI Chatbots

Personal Assistants

Customer Support Systems

LLM Experimentation Playground

Educational AI Tools

<b>How It Works </b>

User input is captured via CLI or Streamlit UI

LangChain processes the prompt and manages context

Request is routed to:

Local LLM via Ollama OR

Groq-hosted model for fast responses

Response is generated and returned with conversation memory

<b>Goals </b>

Provide a fully open-source alternative to closed AI systems

Enable local + cloud hybrid LLM workflows

Make LLM-based app development simple and scalable
