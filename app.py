from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Stop-Motion Desk Pro', page_icon='🎬', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>#MainMenu,header,footer{visibility:hidden} .block-container{padding:0!important;max-width:none!important}</style>''', unsafe_allow_html=True)
html = Path(__file__).with_name('editor.html').read_text(encoding='utf-8')
components.html(html, height=1100, scrolling=True)
