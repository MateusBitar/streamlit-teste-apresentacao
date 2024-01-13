import streamlit as st
import pandas as pd
import base64

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


st.dataframe(
    df[["rank","nome", "apelido", "foto"]],
    column_config={
        "foto": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
            )
        },
    hide_index=True,
    )

df = df.drop([6])
# Escrever o DataFrame de volta para o arquivo CSV
df.to_csv(nome_arquivo, index=False)
