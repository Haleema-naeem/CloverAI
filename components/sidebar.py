import os
import streamlit as st
from config import DOCUMENTS_PATH


def render_sidebar():

    pdf_count = 0

    if os.path.exists(DOCUMENTS_PATH):
        pdf_count = len(
            [f for f in os.listdir(DOCUMENTS_PATH) if f.endswith(".pdf")]
        )

    with st.sidebar:

        st.title("🍀 Clover AI")

        st.success("🟢 System Ready")

        st.divider()

        st.markdown("### 🤖 AI Model")
        st.info("Llama 3.2")

        st.markdown("### 🧠 Embeddings")
        st.info("BGE Small")

        st.markdown("### 📦 Vector Store")
        st.info("ChromaDB")

        st.markdown("### 📄 Documents")
        st.info(f"{pdf_count} Loaded")

        st.divider()

        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()