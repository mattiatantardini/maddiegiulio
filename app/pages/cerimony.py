import streamlit as st

from app.utils import styled_write


def cerimony():

    st.image("resources/images/casa_maddiegiulio_crop3.jpeg")
    styled_write("Siamo felici di annunciare", custom_font_class="title", centered=True)
    styled_write("il nostro matrimonio", custom_font_class="title", centered=True)

    styled_write("Giovedì 31 Ottobre 2024 - Ore 11.00", centered=True)
    styled_write("presso il santuario", centered=True)
    styled_write("Santa Maria del monte di Varese.", centered=True)
    st.divider()
    styled_write(
        "Sarà possibile parcheggiare presso "
        + "<a href='https://maps.app.goo.gl/U5AbkMYpwP3MQm9u6?g_st=com.google.maps.preview.copy'>piazzale Poliaghi</a> "
        + "e sulla via che procede verso il santuario.",
        centered=True,
    )
    styled_write(
        "Lasciata l’auto, occorrerà camminare 5 minuti circa per raggiungere la chiesa. Per chi avesse "
        + "necessità, prima delle scalinate che conducono al santuario, sono presenti due ascensori "
        + "che permettono di “guadagnare” la cima senza salire alcun gradino.",
        centered=True,
    )

    st.write("")
    st.write("")
    st.write("")
    styled_write(
        "“Ma allora che ci guadagni?”", centered=True, custom_font_class="citation"
    )
    styled_write(
        "“Ci guadagno”, disse la volpe,", centered=True, custom_font_class="citation"
    )
    styled_write("“il colore del grano”.", centered=True, custom_font_class="citation")

    st.write("")
    st.write("")
    st.write("")
