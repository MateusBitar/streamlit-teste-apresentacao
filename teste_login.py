import pandas as pd
import streamlit as st


df = pd.read_csv("tenistas.csv")

df.columns = ["nome", "usuario", "senha", "rank", "apelido" ]

novalinha = {"nome": "Georges Bitar", "usuario" : "Georges", "senha" : "senha", "rank": 5, "apelido": "Papai Georges" }
df = pd.concat([df, pd.DataFrame([novalinha])], ignore_index=True)

def main():
    st.title("Tela de Login")

    # Criando campos de entrada para usuário e senha
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    # Verificando se o botão de login foi pressionado
    if st.button("Login"):
        # Simples verificação de usuário e senha
        if not tenistas_df.empty and \
           (df['usuario'] == username).any() and \
           (df['senha'] == password).any():
            st.success("Login bem-sucedido!")
            # Adicione aqui o redirecionamento ou ações que você deseja após o login
        else:
            st.error("Usuário ou senha incorretos.")


if __name__ == "__main__":
    main()
