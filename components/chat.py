import time
import streamlit as st
from rag import ask


def render_chat():

    if len(st.session_state.messages) == 0:

        st.markdown("""
        ## 👋 Welcome to Clover AI!

        Ask anything about your PDF documents.

        ### Try asking:

        • Summarize this document.

        • What are the main topics?

        • Explain what is malware

        • List important points
        """)

    for message in st.session_state.messages:

        avatar = "👤" if message["role"] == "user" else "🍀"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything about your documents...")

    if not prompt:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🍀"):

        start = time.time()

        with st.spinner("🍀 Searching your documents..."):

            answer, sources = ask(prompt)

        elapsed = time.time() - start

        st.markdown(answer)

        if sources:

            with st.expander("📄 Sources Used"):

                shown = set()

                for doc in sources:

                    source = doc.metadata.get("source", "Unknown")

                    if source not in shown:
                        shown.add(source)
                        st.write("•", source)

        st.caption(f"⚡ Response Time: {elapsed:.2f} sec")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
