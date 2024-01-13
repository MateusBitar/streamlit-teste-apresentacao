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



st.title("Página de Cadastro")

# Criar campos de entrada para nome, usuário, senha e apelido
nome = st.text_input("Nome")
novo_usuario = st.text_input("Novo Usuário")
nova_senha = st.text_input("Nova Senha", type="password")
apelido = st.text_input("Apelido")
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png", "gif", "bmp"])

# Verifica se uma imagem foi carregada
if uploaded_file is not None:
    # Exibe a imagem carregada
    st.image(uploaded_file, caption="Imagem carregada", use_column_width=True)

    # Processamento adicional da imagem, se necessário
    # Exemplo: extraindo informações da imagem
    image_info = {"Tipo": uploaded_file.type, "Tamanho": uploaded_file.size}
    st.write("Informações da Imagem:", image_info)

    foto_bi = f"data:image/png;base64,{image_to_base64(uploaded_file)}"

# Verificar se o botão de cadastro foi pressionado
if st.button("Cadastrar"):
    try:
        # Adicionar nova linha ao DataFrame com os dados do novo usuário
        if not nome or not novo_usuario or not nova_senha or not apelido:
            st.warning("Todos os campos são obrigatórios. Preencha todos os campos antes de cadastrar.")
        else:
            # Adicionar nova linha ao DataFrame com os dados do novo usuário
            nova_linha = {'usuario': novo_usuario, 'senha': nova_senha, 'nome': nome, 'apelido': apelido,
                          'foto': foto_bi}
            nova_linha = pd.DataFrame([nova_linha])
            nova_linha['rank'] = len(df) + 1
            df = pd.concat([df, nova_linha], ignore_index=True)

            df.to_csv("tenistas.csv", index=False)

            st.success("Cadastro bem-sucedido! Faça o login para continuar.")
            st.switch_page("Login.py")

            # Adicionando um pequeno delay antes de redirecionar para a página de login
            st.experimental_rerun()
    except Exception as e:
        st.error(f"Erro durante o cadastro: {e}")

