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
        if not df.empty and \
           (df['usuario'] == username).any() and \
           (df['senha'] == password).any():
            st.success("Login bem-sucedido!")
            # Adicione aqui o redirecionamento ou ações que você deseja após o login
        else:
            st.error("Usuário ou senha incorretos.")
            
    if st.button("Cadastre-se", key="cadastre-se-button"):
        cadastro()


def cadastro():
    st.title("Página de Cadastro")

    # Criar campos de entrada para nome, usuário, senha e apelido
    nome = st.text_input("Nome")
    novo_usuario = st.text_input("Novo Usuário")
    nova_senha = st.text_input("Nova Senha", type="password")
    apelido = st.text_input("Apelido")

    # Verificar se o botão de cadastro foi pressionado
    if st.button("Cadastrar"):
        # Adicionar nova linha ao DataFrame com os dados do novo usuário
        if not nome or not novo_usuario or not nova_senha or not apelido:
           st.warning("Todos os campos são obrigatórios. Preencha todos os campos antes de cadastrar.")
        else:
           # Adicionar nova linha ao DataFrame com os dados do novo usuário
           novalinha = {'usuario': novo_usuario, 'senha': nova_senha, 'nome': nome, 'apelido': apelido}
           global df 
           df = pd.concat([df, pd.DataFrame([novalinha])], ignore_index=True)
        
        df.to_csv("tenistas.csv", index=False)

        st.success("Cadastro bem-sucedido! Faça o login para continuar.")

if __name__ == "__main__":
    main()
