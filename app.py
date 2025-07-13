#Bibliotecas importadas


import streamlit as st          #streamlit
import pandas as pd             #pandas para trabalhar com dados e tabelas
import numpy as np 
import matplotlib.pyplot as plt #usada na hora de plotar grafico dizendo qual o tipo de gráfico eu quero.
import altair as alt

###----------------------------------###

#Exemplos de textos. Títulos, subtitulos e etc...
st.title('Oi, Streamlit')
st.write('Tela inicial')
st.header('Titulo')
st.subheader('Subtitulo')
st.text('texto simples')
st.markdown('Formatação editável **negrito** e *italico* por exemplo.')

###----------------------------------###

#Tabela digitada manualmente
data = {
    'Nome': ['Ana','Bruno','Carlos'],
    'Idade':[23,25,45],
    'Salário': [5000, 7000, 9000]
    }
#Colocando a tabela digitada numa variável
df = pd.DataFrame(data)
#Chamando a Variavel num Data Frame (Modelo de tabela onde u usuário pode ordernar coluna, baixar os dados ocultar uma coluna e etc...)
st.dataframe(df)
#Chamando a Variável como tabela (Modelo sem personalização do usuário)
st.table(df)
#Criando tabela com texto antes e depois
st.write('Texto antes da tabela:', df, 'Texto Depois da tabela.')

###----------------------------------###

#Plotando a variável num gráfico de barras, colocando o nome no eixo X e salário no eixo Y
fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salário'])
st.pyplot(fig)

##Gráficos com a Biblioteca Altair
data = pd.DataFrame({
    'categoria': ['A', 'B', 'C', 'D'],
    'valor': [23, 45, 12, 67]
})

# Gráfico dispersão com a Biblioteca Altair
chart = alt.Chart(data).mark_bar().encode(
    x='categoria',
    y='valor'
)
chart
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

###----------------------------------###

#Apenas solta balões na tela
st.balloons()

###----------------------------------###

## Criando um botão e mudando o texto quando o botão é ativado
st.header('st.button')
if st.button('Diga Olá!'):
    st.write('Até Logo! 👋')
else:
    st.write('Olá! 👍')

