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

    df = df.drop(df.index[6])
    
    # Escrever o DataFrame de volta para o arquivo CSV
    df.to_csv(nome_arquivo, index=False)

    


if __name__ == "__main__":
    main()
