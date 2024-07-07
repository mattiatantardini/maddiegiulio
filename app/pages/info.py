import streamlit as st

from app.utils import styled_write


def info():

    styled_write("Ci sposiamo!", custom_font_class="title", centered=True)
    styled_write(
        "Qui troverai le informazioni su come festeggiare con noi.", centered=True
    )
    st.write("")

    if st.button("Festeggia con noi!", use_container_width=True):
        st.balloons()
