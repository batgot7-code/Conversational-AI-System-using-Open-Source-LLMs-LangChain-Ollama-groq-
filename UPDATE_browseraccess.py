import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

llm = ChatGroq(
    temperature=0,
    groq_api_key = 'PLEASE ENTER YOUR API KEY, I CAN\'SHARE MINE',
    model="llama-3.1-8b-instant"
    
)

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