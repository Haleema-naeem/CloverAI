import streamlit as st


def render_header():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#102418,#173322);
        padding:30px;
        border-radius:18px;
        border:1px solid rgba(88,214,141,.25);
        margin-bottom:25px;
    ">

    <h1 style="
        margin:0;
        color:white;
        font-size:42px;
    ">
        🍀 Clover AI
    </h1>

    <p style="
        margin-top:12px;
        color:#B3C2B8;
        font-size:18px;
    ">
        AI-Powered Document Assistant
    </p>

    <p style="
        color:#7DFFB3;
        margin-top:18px;
        font-size:15px;
    ">
        Chat with your PDF documents using local Retrieval-Augmented Generation.
    </p>

    </div>
    """, unsafe_allow_html=True)