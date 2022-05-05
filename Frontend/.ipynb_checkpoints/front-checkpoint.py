from copyreg import dispatch_table
import string
from tkinter import Image
from tkinter.tix import IMAGETEXT
from pyparsing import col
import spacy
import streamlit as st;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import plotly.express as px;
from nltk.corpus import stopwords;
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from wordcloud import WordCloud;
import plotly.express as px


# Adicionando estilo CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


# Carregando os dataset
@st.cache
def load_itens_ilegais():
    df_itens_ilegais = pd.read_csv("../data/df_itens_ilegais.csv")

    return df_itens_ilegais
#fim do carregamento dos dados
@st.cache
def importa_lic():
    dtypes = {'Modalidade Compra':'category','Nome UG':'category','Situação Licitação':'category'}
    df = pd.read_csv("../data/lic_taguiado.csv",dtype=dtypes)
    return df
# Lendo os Dataset
st.cache(persist=True)

df_itens_ilegais = load_itens_ilegais()
df = importa_lic()
menu = ["Pagina Principal", "Licitações", "Participantes", "Itens", "Licitações por Estado"]

with st.sidebar:

    visualizacoes = st.selectbox("Selecione", menu, 0)
if visualizacoes == "Pagina Principal":
    st.title("Licitações Públicas")
    st.text('Essa plataforma foi desenvolvida para que seja utilizada como ferramenta auxiliadora\n na detecção de possíveis indicíos de irregularidades em licitações públicas\ne no combate a corrupção.Você pode visualizar quais os participantes\n e itens mais recorrentes nas licitações com indícios de irregularidades,\n como também, visualizar os estados com maior recorrência de fraude, etc.')
    st.image('..\data\itens_ilegais.png', width=800)
    st.text('')
    st.text('Equipe: \nEdnael Vieira\nGabriel Arnaud de Melo Fragoso\nLiviany Reis Rodrigues')
    st.text('')
    st.text('')
elif visualizacoes == 'Licitações':
    st.title("Panorama geral de licitações por estado")
    st.text(' Dataframe por Estado')
    st.dataframe(df)
    pd.options.display.float_format = '{:,.4f}'.format
    from src.reports_functions.fraudes_estados import indice_fraude_estado
    fraudes = indice_fraude_estado(df,'2018','2020')
    #print(fraudes.head())
    st.dataframe(fraudes)