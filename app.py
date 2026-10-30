import streamlit as st
from pathlib import Path

st.set_page_config(page_title="The Psychology of Multiplayer", layout="wide")

pages = {
    "15 Frameworks": "index.html",
    "References": "references.html",
    "Appendix": "appendix.html",
}

choice = st.radio("", list(pages.keys()), horizontal=True, label_visibility="collapsed")

html = Path(__file__).parent.joinpath(pages[choice]).read_text()
st.components.v1.html(html, height=900, scrolling=True)
