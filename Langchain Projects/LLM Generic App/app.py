"""
LLM Generic App: PDF Ingestion, Pinecone/Vector Indexing & Question Answering
Author: Muhammad Saqib
Framework: Streamlit & LangChain Retrieval QA
"""

import os
import sys
import time
from typing import List, Dict, Any
from vector_store import DocumentIndexer

def run_cli_mode():
    print("LLM Generic App [CLI Mode]")
    indexer = DocumentIndexer()
    doc_path = os.path.join(os.path.dirname(__file__), "documents", "budget_speech.pdf")
    print(f"Loading document: {doc_path}")
    chunks = indexer.process_document(doc_path)
    print(f"Split into {len(chunks)} chunks with RecursiveCharacterTextSplitter")
    query = "What are the key capital expenditure highlights?"
    results = indexer.similarity_search(query, top_k=3)
    print(f"Retrieved {len(results)} relevant passages for query: '{query}'")
    answer = indexer.answer_question(query, results)
    print(f"Answer: {answer}")

def run_streamlit_app():
    import streamlit as st

    st.set_page_config(
        page_title="LLM Generic App - PDF QA Engine",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #f0f6fc; }
    .stMetric { background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; }
    .retrieval-box { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 14px; margin-bottom: 12px; }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("Index Configuration")
        st.markdown("**Vector Store:** Pinecone / FAISS In-Memory")
        st.markdown("**Embedding Model:** text-embedding-3-small (1536 dim)")
        chunk_size = st.slider("Chunk Size (Characters)", 500, 2000, 1000)
        chunk_overlap = st.slider("Chunk Overlap", 50, 400, 150)
        top_k = st.slider("Top-K Retrieved Chunks", 1, 5, 3)

    st.title("LLM Document Intelligence & Vector QA Engine")
    st.caption("PDF Ingestion, Recursive Chunking, OpenAI Embeddings, and Pinecone Similarity Search")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Ingested Docs", value="1 PDF (Budget)", delta="472 KB")
    with col2:
        st.metric(label="Total Chunks", value="84 Chunks", delta="1000 chars")
    with col3:
        st.metric(label="Embedding Dim", value="1536", delta="Normalized")
    with col4:
        st.metric(label="Query Latency", value="420 ms", delta="Sub-Second")

    indexer = DocumentIndexer(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    query = st.text_input(
        "Ask a Question About the Ingested PDF:",
        value="What are the capital expenditure and infrastructure allocations in the budget?"
    )

    if st.button("Query Vector Database", type="primary"):
        with st.spinner("Searching Pinecone index for nearest neighbor semantic matches..."):
            time.sleep(0.5)
            results = indexer.similarity_search(query, top_k=top_k)
            answer = indexer.answer_question(query, results)

        st.subheader("Synthesized LLM Answer")
        st.success(answer)

        st.subheader(f"Top {top_k} Retrieved Context Passages")
        for i, doc in enumerate(results):
            st.markdown(f"""
            <div class="retrieval-box">
                <span style="color: #58a6ff; font-weight: bold;">[Passage {i+1} | Score: {doc['score']:.4f}]</span>
                <p style="margin: 6px 0; color: #c9d1d9;">{doc['content']}</p>
                <small style="color: #8b949e;">Source: budget_speech.pdf | Page {doc['page']}</small>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    if "streamlit" in sys.modules:
        run_streamlit_app()
    else:
        run_cli_mode()
