import streamlit as st
import pandas as pd
def main():
    st.title("Bem Vindo ao ATP Peninsula")

    frase = "Para saber um pouco mais do nosso regulamento clique"
    
    # Texto do link e URL
    link_text = "aqui"
    link_url = "https://regulamentopeninsula.streamlit.app"
    
    # Utilizando .format() para formatar a string
    st.write(f"{frase} [{link_text}]({link_url})")


    


if __name__ == "__main__":
    main()
