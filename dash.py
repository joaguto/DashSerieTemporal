# Mini-Projeto 2 - Data App - Dashboard Financeiro Interativo e em Tempo Real Para Previsão de Ativos Financeiros

# Imports
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from datetime import date
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Define o título do Dashboard
st.title("Conta Nova York")
st.title("Dashboard de Controle da Conta NY")

# Carregando os Dados originais
df = pd.read_excel('Dados_final.xlsx', sheet_name='Planilha1')

# Sub-título
st.subheader('Visualização dos Dados Brutos')
st.write(df.tail())


# Função para o plot dos dados brutos
def plot_dados_brutos():
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=df['TOT DBTS (0)'], x=df['Data'], name="Débitos ao Longo do Tempo"))
    fig.layout.update(title_text='Débitos da Conta NY', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


# Executa a função
plot_dados_brutos()

st.subheader('Previsões com Machine Learning')

# Modelo de série temporal
modelo = SARIMAX(df['TOT DBTS (0)'], order=(9, 2, 3), seasonal_order=(0, 0, 0, 0))

# Treinamento do modelo
resultado = modelo.fit()

# Vamos fazer a previsão dos próximos 15 dias
forecast = resultado.forecast(15)

# Sub-título
st.subheader('Dados Previstos')

# Dados previstos
st.write(resultado.forecast(15).tail())

# Título
st.subheader('Previsão de Débitos da Conta NY')

# Plot
grafico2 = plot_plotly(modelo, forecast)
st.plotly_chart(grafico2)

# Fim
