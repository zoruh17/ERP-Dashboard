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
    print(df_faturado.dtypes)
    return df_faturado

df_faturado = Faturado()

with st.container(border=True):
    faturado = float(df_faturado['Faturado'].iloc[0])
    fig_faturado = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = faturado,
        domain = {'x': [0,1], 'y': [0,1]},
        title = {'text': "Faturado"}))
    st.plotly_chart(fig_faturado)

    devolucao = float(df_faturado['Devolução'].iloc[0])
    fig_devolucao = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = devolucao,
        domain = {'x': [0,1], 'y': [0,1]},
        title = {'text': "Devolução"}))
    st.plotly_chart(fig_devolucao)