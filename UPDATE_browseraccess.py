import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

models = {
    "Llama 3.1 8B Instant": "llama-3.1-8b-instant",
    "Llama 3.3 70B Versatile": "llama-3.3-70b-versatile",
    "Gemma 2 9B": "gemma2-9b-it",
    "DeepSeek R1 Distill Llama 70B": "deepseek-r1-distill-llama-70b",
    "Qwen QWQ 32B": "qwen-qwq-32b"
}

selected_model = st.sidebar.selectbox(
    "🤖 Select AI Model",
    list(models.keys())
)

llm = ChatGroq(
    model=models[selected_model],
    temperature=0,
    groq_api_key="YOUR_GROQ_API_KEY"
)
st.sidebar.success(f"Current Model:\n\n{models[selected_model]}")

prompt = st.text_area('Ask Anything: ')

if st.button('Generate'):
    if prompt:
        with st.spinner('Searching + Generating...'):

            # Step 1: Search web
            search_results = search.run(prompt)

            # Step 2: Combining search result with my prompt
            final_prompt = f"""
            You are an AI assistant with access to web results.

            - Use ONLY relevant info
            - Ignore irrelevant results
            - Be accurate and concise

            Question: {prompt}

            Web Results:
            {search_results}
            """

            # Step 3: Send to LLM
            response = llm.stream(final_prompt)
            st.write_stream(response)