from copyreg import dispatch_table
from optparse import Values
from re import S
import string
from tkinter import Image
from tkinter.tix import IMAGETEXT
from turtle import color
from matplotlib.colors import rgb2hex
from pyparsing import White, col
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

st.set_page_config(
    page_title="Exposer",
    page_icon="✅",
    layout="wide",
)
# Adicionando estilo CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


# Carregando os dataset
@st.cache
def load_itens_ilegais():
    df_itens_ilegais = pd.read_csv("../data/df_itens_ilegais.csv", index_col=[0])

    return df_itens_ilegais
#fim do carregamento dos dados
@st.cache
def importa_lic():
    dtypes = {'Modalidade Compra':'category','Nome UG':'category','Situação Licitação':'category'}
    df = pd.read_csv("../data/lic_taguiado.csv",dtype=dtypes, index_col=[0])
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
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write('')
    with col2:
       st.image('..\data\itens_ilegais.png', width=500)
    with col3:
        st.write('')
    with col4:
        st.write('')

    st.text('Equipe: \nEdnael Vieira\nGabriel Arnaud de Melo Fragoso\nLiviany Reis Rodrigues')

elif visualizacoes == 'Itens':
    st.title("Distribuição dos itens por estado")
    st.text('')
    data_inic = st.text_input("Digite a data inicial para análise (no formato aaaa--mm--dd)")
    data_fim = st.text_input("Digite a data final para análise (no formato aaaa--mm--dd)")
    estado = st.text_input("Digite de qual estado deseja obter informações")

    dd2=df[(df['data']>=data_inic) & (df['data']<=data_fim)]
    gp1=dd2[['UF','Objeto']].groupby(['UF','Objeto'],as_index=False).value_counts()
    st.text('Itens mais licitados por Estado')
    gp2=gp1[gp1['UF']==estado]
    #cont=0
    
    gp2=gp2[0:20]
    from src.reports_functions.plots import plot_lista_objetos
    fig=plot_lista_objetos(gp2)
    st.plotly_chart(fig,width=800)
    st.dataframe(gp2,1500,500)
    

elif visualizacoes == 'Participantes':
    st.title("Seção de Rankings")
    st.text('')
    #data_inic = st.text_input("Digite a data inicial para análise (no formato aaaa--mm--dd)")
    #data_fim = st.text_input("Digite a data final para análise (no formato aaaa--mm--dd)")
    from src.feature_engeneering._03_plus_times_total import calcula_pct_teto
    dd2=df[df['Tag']==0]
    abc = pd.DataFrame(calcula_pct_teto(dd2))
    dd2['pct_do_teto']=abc[0].values

    from src.reports_functions.plots import plot_plus_total
    plus_total=plot_plus_total(dd2)
    st.plotly_chart(plus_total)

    #st.dataframe((dd2.drop(['Código Modalidade Compra','Situação Licitação','Código Órgão','Data Abertura'],axis=1)).iloc[:, 2:].sort_values(by='pct_do_teto',ascending=False)[0:10])

elif visualizacoes == 'Licitações por Estado':

    #dado filtrado
    # dataframe filter
    #df = df[df["UF"] == estado_filtro]

    st.title("Panorama geral de licitações por estado")
    st.text('')
    pd.options.display.float_format = '{:,.4f}'.format

    data_inic = st.text_input("Digite a data inicial para análise (no formato aaaa--mm--dd)")
    data_fim = st.text_input("Digite a data final para análise (no formato aaaa--mm--dd)")

    from src.reports_functions.fraudes_estados import indice_fraude_estado
    fraudes = indice_fraude_estado(df,data_inic,data_fim)
    #st.dataframe(fraudes)
    #print(fraudes.head())
    from src.reports_functions.plots import plot_bar_valores

    config = {
    'toImageButtonOptions': {
    'format': 'webp', # one of png, svg, jpeg, webp
    'filename': 'custom_image',
    'height': 800,
    'width': 900,
    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
    }
    }

    fig1=plot_bar_valores(fraudes,1)
    st.plotly_chart(fig1, use_container_width=False, config=config)
    fig2=plot_bar_valores(fraudes,2)
    st.plotly_chart(fig2, use_container_width=False, config=config, width=800)

    from src.reports_functions.plots import plota_treemap_itens
    treemap = plota_treemap_itens(df,data_inic,data_fim)
    st.plotly_chart(treemap, use_container_width=False)

    st.markdown("\n")

    df2=df.drop(['Código Modalidade Compra','Código UG','Código Órgão Superior','Código Órgão'],axis=1)
    st.markdown("**Visão de detalhada dos dados**", unsafe_allow_html=True)
    st.dataframe(df2)
