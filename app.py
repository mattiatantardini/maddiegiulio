import streamlit as st
from tantaroba.log import configure_logging

from app.pages.cerimony import cerimony
from app.pages.presents import presents


if __name__ == "__main__":
    configure_logging()

    cerimony_page = st.Page(cerimony, title="Cerimonia")
    presents_page = st.Page(presents, title="Facci un regalo :)")

    current_page = st.navigation(pages=[cerimony_page, presents_page])
    st.set_page_config(
        page_title="Maddi e Giulio",
        page_icon=":fallen_leaf:",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.logo("resources/images/casa_maddiegiulio_crop3.jpeg")

    # Allow using custom font
    with open("./resources/css/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

    # Run the selected page
    current_page.run()
