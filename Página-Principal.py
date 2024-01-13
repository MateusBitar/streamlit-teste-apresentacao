import streamlit as st
import pandas as pd
def main():
    st.title("Bem Vindo ao ATP Peninsula")
    link_text = "Para saber um pouco mais do nosso regulamento clique aqui:"
    link_url = "https://regulamentopeninsula.streamlit.app){:target='_blank'"
    st.markdown(f"[{link_text}]({link_url}){:target='_blank'}")

    # Ou usando concatenação de strings
    st.write("[{}]({}){:target='_blank'}".format(link_text, link_url))


if __name__ == "__main__":
    main()
