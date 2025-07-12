import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Oi, Streamlit')
st.write('Tela inicial')

st.header('Titulo')
st.subheader('Subtitulo')

st.balloons()

st.text('texto simples')

st.markdown('Formatação editável **negrito** e *italico* por exemplo.')

data = {
    'Nome': ['Ana','Bruno','Carlos'],
    'Idade':[23,25,45],
    'Salário': [5000, 7000, 9000]
    }

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salário'])
st.pyplot(fig)

