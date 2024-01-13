import streamlit as st
import pandas as pd
import base64

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


# Ler o CSV com os dados dos tenistas ou criar um DataFrame vazio se o arquivo não existir
df = pd.read_csv("tenistas.csv")
df = df.sort_values(by="rank")


def image_to_base64(uploaded_file):
    if uploaded_file is not None:
        # Lê os bytes do arquivo carregado
        file_content = uploaded_file.read()
        # Codifica os bytes em base64
        base64_encoded = base64.b64encode(file_content).decode('utf-8')
        return base64_encoded
    return None


# Função para converter base64 em imagem
def base64_to_image(base64_str):
    return base64.b64decode(base64_str)

st.title("Tela do Ranking")


st.dataframe(
    df[["rank", "foto","apelido"]],
    column_config={
        "foto": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
            )
        },
    hide_index=True,
    )
