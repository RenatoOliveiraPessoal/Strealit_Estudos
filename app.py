import pandas as pd
import streamlit as st
import gspread
import json
from google.oauth2.service_account import Credentials

# Escopos para Google Sheets/Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Carrega credenciais do Streamlit Secrets
creds_info = json.loads(st.secrets["gcp_service_account"]["json"])
creds = Credentials.from_service_account_info(creds_info, scopes=scope)

# Autorizando gspread
client = gspread.authorize(creds)

# Abrindo planilha e aba
spreadsheet = client.open("Respostas NR1")
sheet = spreadsheet.worksheet("Página1")

# Lendo dados e mostrando no app
data = sheet.get_all_records()
st.write(data)

# === Perguntas ===
perguntas = [
    # Grupo 1 - Respeito
    "Você sente que já foi tratado de forma desrespeitosa ou humilhante em seu ambiente de trabalho?",
    "Alguém já fez comentários ofensivos ou depreciativos direcionados a você?",
    "Você já percebeu atitudes de intimidação ou constrangimento contra você?",
    "Já sentiu que sua opinião foi ridicularizada ou desvalorizada intencionalmente?",
    "Você já foi alvo de tratamento discriminatório (por qualquer motivo) em seu ambiente de trabalho?",
    
    # Grupo 2 - Clareza e orientações
    "Você já ficou sem saber claramente o que era esperado do seu trabalho?",
    "Já recebeu tarefas sem orientação suficiente sobre como realizá-las?",
    "Você já sentiu que suas responsabilidades não estavam bem definidas?",
    "Já teve dificuldade em entender os critérios pelos quais seu trabalho seria avaliado?",
    "Você já sentiu que as instruções recebidas foram contraditórias ou confusas?",

    # Grupo 3 - Utilização de habilidades
    "Você já sentiu que tinha pouco trabalho a realizar em comparação com seu tempo disponível?",
    "Já teve a impressão de que suas habilidades não estavam sendo utilizadas?",
    "Você já sentiu que suas tarefas eram simples demais para sua capacidade?",
    "Já percebeu que a falta de atividade no trabalho lhe causava tédio ou desmotivação?",
    "Você já pensou que poderia contribuir mais, mas não recebeu oportunidades para isso?",

    # Grupo 4 - Justiça e equidade
    "Você já sentiu que as regras ou decisões foram aplicadas de forma desigual?",
    "Já percebeu que algumas pessoas receberam privilégios injustificados?",
    "Você já achou que não teve oportunidade de expor sua versão em uma decisão que o envolvia?",
    "Já teve a sensação de que não existe transparência em processos internos?",
    "Você já se sentiu tratado de forma injusta em comparação a outras pessoas?",

    # Grupo 5 - Reconhecimento
    "Você já sentiu que seu esforço não foi valorizado?",
    "Já teve a sensação de que suas contribuições passaram despercebidas?",
    "Você já realizou um bom trabalho e não recebeu nenhum reconhecimento?",
    "Já percebeu que o retorno recebido não correspondeu ao esforço investido?",
    "Você já sentiu que sua dedicação não trouxe nenhum benefício concreto?",

    # Grupo 6 - Autonomia
    "Você já sentiu que não tinha liberdade para decidir como realizar suas tarefas?",
    "Já teve a impressão de que seu trabalho era rigidamente controlado?",
    "Você já achou que não podia escolher a melhor forma de organizar sua rotina de trabalho?",
    "Já sentiu que não podia opinar sobre decisões que afetam suas atividades?",
    "Você já percebeu que tinha pouca ou nenhuma autonomia no dia a dia?",

    # Grupo 7 - Ambiente hostil
    "Você já presenciou situações de agressividade verbal ou física em seu ambiente de trabalho?",
    "Já vivenciou algum episódio que lhe causou forte desconforto emocional?",
    "Você já se sentiu ameaçado em seu ambiente de trabalho?",
    "Já esteve envolvido em uma situação que lhe trouxe medo ou insegurança?",
    "Você já percebeu que acontecimentos no trabalho lhe causaram impacto duradouro no bem-estar?",

    # Grupo 8 - Sobrecarga
    "Você já sentiu que tinha mais tarefas do que conseguiria realizar?",
    "Já trabalhou em ritmo acelerado por períodos prolongados?",
    "Você já teve dificuldade em conciliar as exigências do trabalho com seu tempo pessoal?",
    "Já sentiu que a pressão para entregar resultados era excessiva?",
    "Você já percebeu que seu tempo disponível era insuficiente para cumprir todas as demandas?",

    # Grupo 9 - Apoio
    "Você já precisou de ajuda e não encontrou apoio de colegas ou superiores?",
    "Já sentiu que não podia contar com orientação adequada?",
    "Você já percebeu que, mesmo em dificuldades, teve que lidar sozinho com tudo?",
    "Já teve a sensação de que seu ambiente de trabalho não era colaborativo?",
    "Você já se sentiu desamparado em momentos de maior necessidade?",

    # Grupo 10 - Clima organizacional
    "Você já vivenciou discussões frequentes ou conflitos não resolvidos?",
    "Já sentiu que havia hostilidade no ambiente de trabalho?",
    "Você já percebeu que a comunicação entre as pessoas era marcada por desentendimentos?",
    "Já se sentiu excluído de interações sociais no trabalho?",
    "Você já achou que o clima no ambiente estava constantemente tenso?",

    # Grupo 11 - Mudanças
    "Você já vivenciou mudanças no trabalho sem explicações claras?",
    "Já sentiu que não foi informado adequadamente sobre alterações importantes?",
    "Você já percebeu que mudanças foram implementadas de forma repentina e confusa?",
    "Já se sentiu inseguro diante de mudanças porque não recebeu orientações suficientes?",
    "Você já achou que as mudanças não tiveram acompanhamento adequado?",

    # Grupo 12 - Comunicação
    "Você já sentiu que não recebia informações essenciais a tempo?",
    "Já teve dificuldade em obter respostas para dúvidas importantes?",
    "Você já percebeu falhas frequentes na troca de informações entre pessoas?",
    "Já se sentiu prejudicado pela falta de clareza na comunicação?",
    "Você já teve problemas por não receber instruções completas?",

    # Grupo 13 - Isolamento
    "Você já sentiu que trabalhar de forma isolada prejudicou sua convivência social?",
    "Já percebeu que a distância dificultava o acesso a informações importantes?",
    "Você já se sentiu desconectado das pessoas com quem trabalha?",
    "Já teve a impressão de que a falta de contato presencial reduzia sua motivação?",
    "Você já achou difícil, em algum momento, manter vínculos sociais por conta do distanciamento?"

]

opcoes = ["Nunca", "Raramente", "Às vezes", "Sempre"]

# === Controle de navegação ===
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
if "setor" not in st.session_state:
    st.session_state.setor = None

# === Página inicial ===
if st.session_state.pagina == "inicio":
    st.title("📌 Projeto de regulamentação e avaliação as normas da NR-1")

    setor = st.selectbox("Informe o seu setor:", 
                         ["Selecione...", "Contabilidade", "Operações", "Financeiro", "RH", "Outro"])

    if st.button("Prosseguir para o questionário"):
        if setor != "Selecione...":
            st.session_state.setor = setor
            st.session_state.pagina = "questionario"
            st.rerun()
        else:
            st.warning("⚠️ Selecione um setor antes de prosseguir.")

# === Página do questionário ===
elif st.session_state.pagina == "questionario":
    st.title("📋 Questionário de Percepções no Trabalho")
    st.write(f"Setor informado: **{st.session_state.setor}**")

    # Inicializa estado se necessário
    if "indice_pergunta" not in st.session_state:
        st.session_state.indice_pergunta = 0
    if "respostas" not in st.session_state:
        st.session_state.respostas = {}

# Pergunta atual
idx = st.session_state.indice_pergunta
pergunta_atual = perguntas[idx]

# Mostra progresso
st.write(f"Pergunta {idx + 1} de {len(perguntas)}")

# Seleção de resposta
resposta = st.radio(pergunta_atual, opcoes, index=None, key=f"q_{idx}")

# Botão Próxima
if st.button("Próxima"):
    if resposta is None:
        st.warning("⚠️ Selecione uma opção antes de continuar.")
    else:
        st.session_state.respostas[pergunta_atual] = resposta
        st.session_state.indice_pergunta += 1

# Mostra a próxima pergunta ou envia respostas
if st.session_state.indice_pergunta >= len(perguntas):
    linha = [st.session_state.setor, pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")]
    linha.extend([st.session_state.respostas[p] for p in perguntas])
    sheet.append_row(linha)
    st.success("✅ Respostas enviadas com sucesso!")
    st.balloons()
    st.session_state.pagina = "inicio"
    st.session_state.indice_pergunta = 0
    st.session_state.respostas = {}


                # Resetar questionário
                st.session_state.pagina = "inicio"
                st.session_state.indice_pergunta = 0
                st.session_state.respostas = {}
                st.experimental_rerun()
