import streamlit as st
from tantaroba.log import configure_logging
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud


@st.experimental_dialog("Aggiungi persone")
def add_names():
    st.write("Quanti nomi vuoi inserire?")
    n = st.number_input("Numero di nomi", value=1, step=1)

    for i in range(0, n):
        st.text_input("Inserisci nome", key=f"name_{i}")

    ok = st.button("Salva")
    if ok:
        st.session_state["names"] += [
            st.session_state[f"name_{i}"] for i in range(0, n)
        ]
        st.write(st.session_state["names"])
        st.rerun()


if __name__ == "__main__":
    configure_logging()

    st.set_page_config(
        page_title="Maddi e Giulio",
        page_icon=":smile:",
        layout="centered",
    )

    if "names" not in st.session_state:
        st.session_state["names"] = ["Maddi Giulio"]

    with open("./style/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.write("ciao")

    _, mid_col, _ = st.columns([1, 1, 1])
    with mid_col:
        st.markdown("<div class=title>Ci sposiamo!</div>", unsafe_allow_html=True)

    st.markdown("Fai un regalo qui:")
    st.markdown("## IT XXXX 000111222")

    text = "Maddi Giulio Mattia Detta Gio Ermi Lele Franci Tommi Nico Fede Andrea Grazia Chiara Giulia Martina Sara Mattia Francesco Marco Matteo Alice Erica Giovanna Anna"

    st.write("Se hai fatto un regalo, aggiungi il tuo nome.")
    add_names_button = st.button("Aggiungi il tuo nome")
    if add_names_button:
        add_names()

    mask = np.array(Image.open("./casa_mask.png"))
    wc = WordCloud(
        # font_path=path/to/font
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
    fig = wc.generate(" ".join(st.session_state["names"]))
    # fig = wc.to_image()

    # contour = draw_contour(wc.to_image(), wc.mask, 1, 'black')
    # print(contour)
    # contour.show()

    plt.figure(figsize=(80, 60), frameon=False)
    plt.imshow(fig)
    plt.axis("off")
    plt.savefig("casa1.png")

    st.image("casa1.png", width=800)
