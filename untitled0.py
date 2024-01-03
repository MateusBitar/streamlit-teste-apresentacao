# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:42:22 2024

@author: andre
"""

import streamlit as st

def main():
    st.title("Tela de Login")

    # Criando campos de entrada para usuário e senha
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    # Verificando se o botão de login foi pressionado
    if st.button("Login"):
        # Simples verificação de usuário e senha (substitua isso por sua lógica de autenticação real)
        if username == "usuario" and password == "senha":
            st.success("Login bem-sucedido!")
            # Adicione aqui o redirecionamento ou ações que você deseja após o login
        else:
            st.error("Usuário ou senha incorretos.")

if __name__ == "__main__":
    main()
