import datetime

import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from psqlpandas.postgresql import PostgresqlDatabaseConnector

from settings.config import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_PWD,
    POSTGRES_USER,
)
from app.utils import styled_write


@st.cache_resource
def get_connection():
    return PostgresqlDatabaseConnector(
        dbname=POSTGRES_DBNAME,
        host=POSTGRES_HOST,
        user=POSTGRES_USER,
        port=POSTGRES_PORT,
        password=POSTGRES_PWD,
    )


@st.cache_resource
def generate_wordcloud(names):
    mask = np.array(Image.open("resources/images/casa_maddiegiulio_nera_ok.png"))
    wc = WordCloud(
        font_path="resources/fonts/Typo.ttf",
        width=3000,
        height=2000,
        max_words=40,
        random_state=1,
        background_color="white",
        contour_color="black",
        contour_width=1,
        colormap="OrRd_r",  # Change this to change text colors: see here: https://www.kaggle.com/code/niteshhalai/wordcloud-colormap
        collocations=True,
        normalize_plurals=True,
        mask=mask,
    )
    fig = wc.generate(names)

    plt.figure(figsize=(80, 60), frameon=False)
    plt.imshow(fig)
    plt.axis("off")
    plt.savefig("resources/images/home_wordcloud.png")


@st.dialog("Costruisci la casa")
def add_names(db_conn: PostgresqlDatabaseConnector):
    with st.form("new_name"):
        st.write(
            "Scrivi il tuo nome (se siete in più di uno, scrivi i nomi separati da spazi):"
        )
        name = st.text_input("Inserisci il tuo nome")
        st.write("Se vuoi, lascia un messaggio per gli sposi:")
        message = st.text_area("Inserisci il tuo messaggio")
        ok = st.form_submit_button("Salva", use_container_width=True)
        if ok:
            with st.spinner("Salvataggio in corso"):
                db_conn.execute_sql_query(
                    "INSERT INTO names_new (name, message, date_saved) VALUES (%s, %s, %s)",
                    (name, message, datetime.datetime.now()),
                )
            st.rerun()


def presents():

    db_conn = get_connection()

    df = db_conn.read_df("SELECT name FROM names_new")
    names = df["name"].str.split(" ").explode().str.capitalize().to_list()
    # Cleaning (removes 1-character words)
    names = [n for n in names if len(n) > 1]

    generate_wordcloud(" ".join(names))
    st.image("resources/images/home_wordcloud.png", use_column_width="always")

    styled_write(
        "Se ti va, puoi aiutarci a costruire un pezzetto di casa.",
        centered=True,
    )
    styled_write(
        "Grazie fin da ora!",
        centered=True,
    )
    styled_write(
        "IT71N0306951270100000061566",
        centered=True,
        custom_font_class="iban",
        add_space_after=True,
    )

    add_names_button = st.button(
        "Aggiungi il tuo nome alla casa", use_container_width=True
    )
    if add_names_button:
        add_names(db_conn)
