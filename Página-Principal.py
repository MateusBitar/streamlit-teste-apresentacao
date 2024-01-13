import streamlit as st
import pandas as pd
def main():
    st.title("Bem Vindo ao ATP Peninsula")

    frase = "Para saber um pouco mais do nosso regulamento clique"
    
    # Texto do link e URL
    link_text = "aqui"
    link_url = "https://regulamentopeninsula.streamlit.app"
    
    # Utilizando .format() para formatar a string
    texto_completo = "{} [{}]({}){{:target='_blank'}}".format(frase, link_text, link_url)
    
    # Exibindo no Streamlit
    st.write(texto_completo)


if __name__ == "__main__":
    main()
