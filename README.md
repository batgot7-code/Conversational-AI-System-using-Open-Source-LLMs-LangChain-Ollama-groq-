# Conversational-AI-System-using-Open-Source-LLMs (LangChain-Ollama/groq)

<b>CONVERSATIONAL AI SYSTEM USING OPEN-SOURCE LLMs </b>

(LangChain + Ollama / Groq)

This project is a lightweight, modular, powerful and flexible Conversational AI system built using open-source Large Language Models (LLMs). It leverages LangChain for orchestration and supports both local inference via Ollama and ultra-fast cloud inference via Groq.

The system is designed to be flexible, efficient, and developer-friendly, making it ideal for building chatbots, assistants, and AI-powered applications without relying on proprietary models.

A key highlight of this system is its browser access capability, enabling the AI to retrieve real-time, up-to-date information from the web, overcoming the static knowledge limitations of traditional LLMs.

<b>FEATURES </b>

<b>NATURAL CONVERSATIONAL INTERFACE </b>

Context-aware multi-turn conversations

<b>LANGCHAIN INTEGRATION </b>

Prompt management, memory handling, and chaining capabilities

<b>DUAL INFERENCE SUPPORT </b>

Ollama → Run LLMs locally (privacy-focused)

Groq → High-speed inference using LPU acceleration

<b>BROWSER ACCESS (LIVE WEB RETREIVAL) </b>

Fetches latest information from the internet for accurate, real-time responses

<b>MODULAR DESIGN </b>

Easily plug in different LLMs (LLaMA, Mistral, Qwen, etc.)

<b>STREAMLIT UI (FAST AND INTERACTIVE) </b>

Simple and interactive frontend for real-time chatting

<b>TECH STACK </b>

Python

LangChain

Ollama (local LLMs)

Groq API (fast inference)

Streamlit (UI)

Web Browsing Tools (for real-time data) -> DUCK DUCK GO

<b>USE CASES </b>

AI Chatbots

Personal Assistants

Customer Support Systems

LLM Experimentation Playground

Educational AI Tools

<b>HOW IT WORKS </b>

User input is captured via CLI or Streamlit UI

LangChain processes the prompt and manages context

Request is routed to:

Local LLM via Ollama OR

Groq-hosted model for fast responses

Response is generated and returned with conversation memory

<b>GOALS </b>

Provide a fully open-source alternative to closed AI systems

Enable local + cloud hybrid LLM workflows

Make LLM-based app development simple and scalable
