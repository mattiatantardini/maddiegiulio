import datetime

import streamlit as st
import pandas as pd
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


@st.experimental_dialog("Aggiungi persone")
def add_names(last_id: int, db_conn: PostgresqlDatabaseConnector):
    with st.form("new_name"):
        st.write(
            "Scrivi il tuo nome (se siete in più di uno, scrivi i nomi separati da spazi):"
        )
        name = st.text_input("Inserisci il tuo nome")
        st.write("Se vuoi, lascia un messaggio per gli sposi:")
        message = st.text_area("Inserisci il tuo messaggio")
        ok = st.form_submit_button("Salva")
        if ok:
            new_row = pd.DataFrame(
                data={
                    "uid": last_id + 1,
                    "name": name,
                    "message": message,
                    "date_saved": datetime.datetime.now(),
                },
                index=[0],
            )
            with st.spinner("Salvataggio in corso"):
                db_conn.insert_from_df("names", new_row)
            st.rerun()


def presents():

    db_conn = get_connection()

    last_uid = int(db_conn.read("SELECT max(uid) FROM NAMES")[0][0])

    styled_write(
        "Questo e' il nostro IBAN (non usiamo la e accentata se possibile, non c'è nel font):",
        centered=True,
        add_space_after=True,
    )
    styled_write(
        "IT00001111122222",
        centered=True,
        custom_font_class="title",
        add_space_after=True,
    )
    styled_write(
        "Se hai fatto un regalo, aggiungi il tuo nome.",
        centered=True,
        add_space_after=True,
    )
    add_names_button = st.button("Aggiungi il tuo nome", use_container_width=True)
    if add_names_button:
        add_names(last_uid, db_conn)

    df = db_conn.read_df("SELECT name FROM names")
    names = df["name"].str.split(" ").explode().str.capitalize().to_list()
    # Cleaning
    names = [n for n in names if len(n) > 1]

    generate_wordcloud(" ".join(names))
    st.image("resources/images/home_wordcloud.png", use_column_width="always")
