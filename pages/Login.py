import streamlit as st
import pandas as pd
import base64

st.title("Tela de Login")

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

if st.session_state.get("logged_in", False):
    st.error("Você já está logado!.")
    st.write("Deseja sair?")
    if st.button("Sim"):
        st.session_state.logged_in = False
        st.experimental_rerun()
    st.stop()

# Criando campos de entrada para usuário e senha
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Verificando se o botão de login foi pressionado
if st.button("Login"):
    # Simples verificação de usuário e senha
    if not df.empty and \
            (df['usuario'] == username).any() and \
            (df['senha'] == password).any():
        st.success("Login bem-sucedido!")
        st.session_state.logged_in = True
        #st.switch_page("pages/Ranking.py")
        
    else:
        st.error("Usuário ou senha incorretos.")
