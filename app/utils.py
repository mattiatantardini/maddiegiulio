import streamlit as st


def styled_write(
    text: str,
    centered: bool = False,
    custom_font_class: None | str = None,
    add_space_after: bool = False,
):
    if not centered and custom_font_class is None:
        st.markdown(text)
    elif centered and custom_font_class is None:
        st.markdown(
            f'<div style="text-align: center">{text}</div>', unsafe_allow_html=True
        )
    elif not centered and custom_font_class is not None:
        st.markdown(
            f"<div class={custom_font_class}>{text}</div>", unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class={custom_font_class} style="text-align: center">{text}</div>',
            unsafe_allow_html=True,
        )

    if add_space_after:
        st.write("")
