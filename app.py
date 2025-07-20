import streamlit as st
import os
from rag import load_split_embeds_stores_pdfs_in_FAISS, get_rag_chain
from tools_agents import create_agent

st.set_page_config(page_title="📚 Multi-PDF RAG + Agent Chatbot")
st.title("Multi-PDF Chat + Smart Agent")

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data", exist_ok=True)
    for file in uploaded_files:
        with open(f"data/{file.name}", "wb") as f:
            f.write(file.read())
    st.success("PDFs Uploaded. Ready to build knowledge base.")

    if st.button("Build RAG + Agent"):
        with st.spinner("Building knowledge base and agent..."):
            vectorstore = load_split_embeds_stores_pdfs_in_FAISS("data/")
            rag_chain = get_rag_chain(vectorstore)
            agent = create_agent()

        st.session_state.rag_chain = rag_chain
        st.session_state.agent = agent
        st.success("Knowledge base + Agent ready!")

# Chat Interface
if "rag_chain" in st.session_state and "agent" in st.session_state:
    question = st.text_input("Ask a question")

    if question:
        with st.spinner("Thinking..."):
            rag_result = st.session_state.rag_chain.invoke({"input": question})
            answer = rag_result.get("answer", "").strip()

        if answer.lower().strip() == "i don't know from the pdf.":
            tool_result = st.session_state.agent.run(question)
            st.markdown(f"**Answer (from tools):** {tool_result}")
        else:
            st.markdown(f"**Answer (from PDFs):** {answer}")

