import shutil
from pathlib import Path

import streamlit as st
from tantaroba.log import configure_logging

from app.pages.info import info
from app.pages.presents import presents


if __name__ == "__main__":
    configure_logging()

    info_page = st.Page(info, title="Informazioni")
    presents_page = st.Page(presents, title="Fai un regalo")

    current_page = st.navigation(pages={"Your title here": [info_page, presents_page]})
    st.set_page_config(
        page_title="Maddi e Giulio",
        page_icon=":fallen_leaf:",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.logo("resources/images/casa_maddiegiulio_crop3.jpeg")

    # Allow using custom font
    streamlit_static_path = Path(st.__path__[0]) / "static"
    font_path = streamlit_static_path / "assets/fonts"
    if not font_path.is_dir():
        font_path.mkdir(exist_ok=True, parents=True)
    for ff in ["typo-webfont.woff2", "typo-webfont.woff", "Typo.ttf"]:
        font_file = font_path / ff
        if not font_file.exists():
            shutil.copy("resources/fonts/typo-webfont.woff2", font_file)

    with open("./resources/css/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

    # Run the selected page
    current_page.run()
