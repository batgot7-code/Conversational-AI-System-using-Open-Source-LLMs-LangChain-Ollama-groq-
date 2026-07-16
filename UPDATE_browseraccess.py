import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# -----------------------------
# Search Tool
# -----------------------------
search = DuckDuckGoSearchRun()

# -----------------------------
# Session State
# -----------------------------
if "search_history" not in st.session_state:
    st.session_state.search_history = []

if "selected_query" not in st.session_state:
    st.session_state.selected_query = ""

# -----------------------------
# Sidebar - Model Selection
# -----------------------------
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

st.sidebar.success(f"Current Model:\n\n{models[selected_model]}")

# -----------------------------
# Sidebar - Search History
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🕒 Search History")

history = list(reversed(st.session_state.search_history))

for i, query in enumerate(history):
    if st.sidebar.button(query, key=f"history_{i}"):
        st.session_state.selected_query = query
        st.rerun()

if st.sidebar.button("🗑 Clear History"):
    st.session_state.search_history.clear()
    st.session_state.selected_query = ""
    st.rerun()

# -----------------------------
# LLM
# -----------------------------
llm = ChatGroq(
    model=models[selected_model],
    temperature=0,
    groq_api_key="YOUR_GROQ_API_KEY"
)

# -----------------------------
# Main UI
# -----------------------------
prompt = st.text_area(
    "Ask Anything:",
    value=st.session_state.selected_query,
    height=120
)

if st.button("Generate"):
    if prompt.strip():

        # Save search history
        if (
            len(st.session_state.search_history) == 0
            or st.session_state.search_history[-1] != prompt
        ):
            st.session_state.search_history.append(prompt)

            # Keep only last 20 searches
            st.session_state.search_history = (
                st.session_state.search_history[-20:]
            )

        with st.spinner("Searching + Generating..."):

            # Step 1: Search web
            search_results = search.run(prompt)

            # Step 2: Create prompt
            final_prompt = f"""
You are an AI assistant with access to web results.

Instructions:
- Use ONLY relevant information.
- Ignore unrelated search results.
- Be accurate and concise.
- If the search results are insufficient, clearly mention it.

Question:
{prompt}

Web Results:
{search_results}
"""

            # Step 3: Generate response
            response = llm.stream(final_prompt)

            st.write_stream(response)