import streamlit as st 
import pandas as pd
import webbrowser
from datetime import datetime

## Configuração da página 
st.set_page_config(
    page_title="🏠Home",
    page_icon="⚽️",
    layout="wide",
)

## Condicional da session state
if "data" not in st.session_state:
    ## Define o dataframe
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    ## Contrato válido de jogadores 
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data
   
st.write("# FIFA 2023 - Data Analysis!⚽️")

## SIDEBAR 
st.sidebar.write("Desenvolvido por: Anderson Seixas Developer")

## Criando botão 
btn = st.button("Acesse os dados no Keggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
    O conjunto de dados de
    jogadores de futebol de 2017 a 2023 fornece informações abrangentes
    sobre jogadores de futebol profissionais. O conjunto de dados contém
    uma ampla gama de atributos, incluindo dados demográficos de jogador,
    características físicas, estatísticas de jogo, detalhes do contrato e
    afiliações de clubes. 

    Com mais de 17.000 registros, este conjunto de dados oferece um
    recurso valioso para analistas defutebol, pesquisadores e entusiastas
    interessados em explorar vários aspectos do mundo do futebol, pois permite estudar
    atributos de jogadores, métricas de desempenho, avaliação de mercado, 
    análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.


    Fontes e conteúdo relacionado

    """
    
)

