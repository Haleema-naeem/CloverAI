import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar
from components.chat import render_chat

st.set_page_config(
    page_title="Clover AI",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    try:
        with open("styles/style.css", "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass


load_css()

if "messages" not in st.session_state:
    st.session_state.messages = []

render_sidebar()
render_header()
render_chat()
