import streamlit as st
import pandas as pd

# Função para autenticar o usuário
def autenticar(usuario, senha, df_usuarios):
    usuario = usuario.strip()
    senha = senha.strip()
    return not df_usuarios[
        (df_usuarios['usuario'] == usuario) &
        (df_usuarios['senha'] == senha)
    ].empty

# Carrega o CSV
def carregar_usuarios(caminho_csv="usuarios.csv"):
    return pd.read_csv(caminho_csv)

# Página de login
def pagina_login():
    st.title("🔐 Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        df_usuarios = carregar_usuarios()
        if autenticar(usuario, senha, df_usuarios):
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")

# Página após login
def pagina_links():
    st.title(f"Bem-vindo, {st.session_state['usuario']}!")
    st.subheader("📊 Relatórios Power BI")

    links = {
        "Relatório 1": "https://app.powerbi.com/view?r=eyJrIjoiYTlhNWUxZjktMmU4OC00Y2E3LWEyN2UtNzBkNzgxNjUyNDY0IiwidCI6IjI4Mzc4MGEwLTliN2QtNGQ1MS1hMDFjLWY4Zjk3NWU2NzY2YiJ9",
        "Relatório 2": "https://link2.com",
        "Relatório 3": "https://link3.com",
        "Relatório 4": "https://link4.com",
        "Relatório 5": "https://link5.com",
        "Relatório 6": "https://link6.com"
    }

    for nome, url in links.items():
        st.markdown(f"[🔗 {nome}]({url})", unsafe_allow_html=True)

    if st.button("Sair"):
        st.session_state.clear()
        st.experimental_rerun()

# Execução principal
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if st.session_state["logado"]:
    pagina_links()
else:
    pagina_login()
