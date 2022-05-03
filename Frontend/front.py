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
    df_itens_ilegais = pd.read_csv("data\df_itens_ilegais.csv")
           
    return df_itens_ilegais

st.cache(persist = True) 

# Lendo os Dataset
df_itens_ilegais = load_itens_ilegais()


menu = ["Pagina Principal", "Licitações", "Participantes", "Itens", "Licitações por Estado"]

with st.sidebar:

    visualizacoes = st.selectbox("Selecione", menu, 0)
if visualizacoes == "Pagina Principal":
    st.title("Licitações Públicas")
    st.text('Essa plataforma foi desenvolvida para que seja utilizada como ferramenta auxiliadora\n na detecção de possíveis indicíos de irregularidades em licitações públicas\ne no combate a corrupção.Você pode visualizar quais os participantes\n e itens mais recorrentes nas licitações com indícios de irregularidades,\n como também, visualizar os estados com maior recorrência de fraude, etc.')
    st.image('data/itens_ilegais.png', width=800)
    st.text('')
    st.text('Equipe: \nEdnael Vieira\nGabriel Arnaud de Melo Fragoso\nLiviany Reis Rodrigues')
    st.text('')
    st.text('')
        
