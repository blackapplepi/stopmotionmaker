import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Stop-Motion Desk Pro", page_icon="🎬", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
header[data-testid="stHeader"] {visibility:hidden;}
footer {visibility:hidden;}
.block-container {padding:0 !important; max-width:none !important;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).with_name("editor.html")
HTML = html_path.read_text(encoding="utf-8")
components.html(HTML, height=1000, scrolling=True)
