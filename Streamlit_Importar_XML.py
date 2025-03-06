import streamlit as st
import os
import shutil

# Caminho da pasta do OneDrive onde os arquivos serão salvos
onedrive_path = r"https://dmparanacombr-my.sharepoint.com/my?id=%2Fpersonal%2Frenato%5Foliveira%5Fdmparana%5Fcom%5Fbr%2FDocuments%2FFerramentas%2FXML%20PENDENTES&FolderCTID=0x0120000A4A3AE61C3B684FB09F795944486215"

# Função para salvar o arquivo no OneDrive
def save_file_to_onedrive(uploaded_file):
    # Verificar se a pasta existe
    if not os.path.exists(onedrive_path):
        st.error(f"A pasta {onedrive_path} não existe!")
        return

    # Salvar o arquivo na pasta do OneDrive
    with open(os.path.join(onedrive_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Arquivo {uploaded_file.name} foi salvo com sucesso no OneDrive!")

# Título da aplicação
st.title("Upload de Arquivo XML")

# Formulário de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo XML", type="xml")

# Se um arquivo for carregado, salva no OneDrive
if uploaded_file is not None:
    save_file_to_onedrive(uploaded_file)
    

