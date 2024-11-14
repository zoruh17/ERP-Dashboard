import pandas as pd
import streamlit as st
import plotly
import plotly.graph_objects as go

st.logo(
    image="images/logo-gala-white.png",
    size="large",
)

st.set_page_config(page_title="Faturamento",layout='wide')

@st.cache_data(ttl=60)
def Faturado():
    df_faturado = pd.read_excel("faturado.xlsx")

    df_faturado['Data'] = df_faturado['Data'].dt.strftime('%d/%m/%Y')

    return df_faturado

df_faturado = Faturado()

fig_faturado = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 'Faturado',
    domain = {'x': [0,1], 'y': [0,1]},
    title = {'text': "Faturado"}))

fig_faturado.show()