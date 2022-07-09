from copyreg import dispatch_table
import gzip
from optparse import Values
from re import S
import string
from tkinter import Image
from tkinter.tix import IMAGETEXT
from turtle import color
from cv2 import normalize
from matplotlib import colors
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
def load_df_g():
    dtyypes = {'Nome UG':'category', 
        'Modalidade Compra':'category', 
        'Número Processo':'category', 
        'Objeto':'category',
       'Nome Órgão Superior':'category', 
        'Código Órgão':'int32', 
        'Nome Órgão':'category', 'Município':'category',
        'Obras':'category', 'Tag':'int32', 'Descrição Item Compra':'category',
       'Nome Participante':'category', 'Flag Vencedor':'category', 'UF':'category'}

    load_df_g = pd.read_csv("../data/df_geral.gzip",compression='gzip',index_col=[0],dtype=dtyypes)

    return load_df_g

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
df_g=load_df_g()
menu = ["Pagina Principal", "Lista dos TOPS", "Itens", "Licitações por Estado"]
config = {'displayModeBar': False}
with st.sidebar:

    visualizacoes = st.selectbox("Selecione", menu, 0)
    data_inic = st.date_input('Insira a data inicial da análise')
    data_fim = st.date_input('Insira a data final da análise')

if visualizacoes == "Pagina Principal":

    st.title("Exposer")
    st.text('Ferramenta de apoio para detecção de irregularidades em liticações públicas')
    dd2=df[(df['data']>=str(data_inic)) & (df['data']<=str(data_fim))]
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        valores = dd2['Tag'].value_counts(normalize=True).round(2)
        #st.write(valores)
        val0= str(valores[0])
        val1= str(valores[1])
        st.metric(label='Qtd de Licitações\nIrregulares',value = dd2['Tag'].value_counts()[0],delta=val0,delta_color="inverse")
        
    with col2:
       st.metric(label='Qtd de Licitações\nNormais',value = dd2['Tag'].value_counts()[1],delta=val1,delta_color="normal")
    with col3:
        vmax ="R$"+str((dd2['Total'].sum()/1000000000).round(1))+' Bi'
        st.metric(label='Valor Licitado no Período',value =vmax)
        #st.image('..\data\itens_ilegais.png', width=500)
    with col4:
        st.write('')
    st.text('Tipos de Licitações presentes')
    st.plotly_chart(px.bar(dd2['Modalidade Compra'].value_counts(),labels={'value':'Quantidade de Licitações','index':'Tipo'},
                    text_auto=True,color='value',color_continuous_scale=px.colors.sequential.Viridis))

    st.text('Equipe: \nEdnael Vieira\nGabriel Arnaud de Melo Fragoso\nLiviany Reis Rodrigues')

elif visualizacoes == 'Itens':
    st.title("Distribuição dos itens por estado")
    st.text('')
    #data_inic = st.text_input("Digite a data inicial para análise (no formato aaaa--mm--dd)")
    #data_fim = st.text_input("Digite a data final para análise (no formato aaaa--mm--dd)")
    estado = st.text_input("Digite a sigla do estado que deseja obter informações")

    dd2=df[(df['data']>=str(data_inic)) & (df['data']<=str(data_fim))]
    gp1=dd2[['UF','Objeto']].groupby(['UF','Objeto'],as_index=False).value_counts()
    st.text('Itens mais licitados por Estado')
    gp2=gp1[gp1['UF']==estado]
    #cont=0
    
    gp2=gp2[0:20]
    from src.reports_functions.plots import plot_lista_objetos
    fig=plot_lista_objetos(gp2)
    st.plotly_chart(fig,width=800)

    pd.options.display.max_rows=200

    st.dataframe(gp2,1500,500)
    

elif visualizacoes == 'Lista dos TOPS':
    st.title("Seção de Rankings")
    st.text('')
    #data_inic = st.text_input("Digite a data inicial para análise (no formato aaaa--mm--dd)")
    #data_fim = st.text_input("Digite a data final para análise (no formato aaaa--mm--dd)")
    from src.feature_engeneering._03_plus_times_total import calcula_pct_teto
    dd2=df[df['Tag']==0]
    abc = pd.DataFrame(calcula_pct_teto(dd2))
    dd2['pct_do_teto']=abc[0].values
    ############
    from src.reports_functions.plots import plot_plus_total
    plus_total=plot_plus_total(dd2)
    st.plotly_chart(plus_total,config=config)
    ############

    #st.text('TOP 10: Empresas que mais perderam processos licitatórios disputados no período')
    top_part=pd.DataFrame(df_g[(df_g["Flag Vencedor"]=='NÃO') & (df_g['Tag']==0)].loc[:,["Nome Participante"]].value_counts().head(10))
    top_part.reset_index(drop=False,inplace=True)
    top_part.rename({0:'Qtd de derrotas'},axis=1,inplace=True)
    top_part=top_part.sort_values(by='Qtd de derrotas')
    from src.reports_functions.plots import plot_tops

    figg=plot_tops(top_part)
    figg.update_layout(title_text='TOP 10: Empresas que mais perderam processos licitatórios disputados no período')
    figg.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)')
    figg.update_yaxes(title='Nome do participante')
    figg.update_xaxes(title='Quantidade')
    st.plotly_chart(figg,config=config)


    #st.text('TOP 10: Empresas que mais venceram processos licitatórios disputados no período')
    top_winners = pd.DataFrame(df_g[(df_g["Flag Vencedor"]== 'SIM') & (df_g['Tag']==0)].loc[:,["Nome Participante"]].value_counts().head(10))
    top_winners.reset_index(drop=False,inplace=True)
    top_winners.rename({0:'Qtd de vitórias'},axis=1,inplace=True)
    top_winners=top_winners.sort_values(by='Qtd de vitórias')
    figg2=plot_tops(top_winners)
    figg2.update_layout(title_text='TOP 10: Empresas que mais venceram processos licitatórios disputados no período')
    figg2.update_traces(marker_color='rgb(255,40,0)', marker_line_color='rgb(8,48,107)',opacity=0.8)
    figg2.update_yaxes(title='Nome do participante')
    figg2.update_xaxes(title='Quantidade')
    st.plotly_chart(figg2,config=config)


elif visualizacoes == 'Licitações por Estado':

    st.title("Panorama geral de licitações por estado")
    st.text('')
    pd.options.display.float_format = '{:,.4f}'.format

    from src.reports_functions.fraudes_estados import indice_fraude_estado
    fraudes = indice_fraude_estado(df,str(data_inic),str(data_fim))

    from src.reports_functions.plots import plot_bar_valores

    fig1=plot_bar_valores(fraudes,1)
    st.plotly_chart(fig1, use_container_width=False, config=config)
    fig2=plot_bar_valores(fraudes,2)
    st.plotly_chart(fig2, use_container_width=False, config=config, width=800)

    from src.reports_functions.plots import plota_treemap_itens
    treemap = plota_treemap_itens(df,str(data_inic),str(data_fim))
    st.plotly_chart(treemap, use_container_width=False)

    st.markdown("\n")

    df2=df.drop(['Código Modalidade Compra','Código UG','Código Órgão Superior','Código Órgão'],axis=1)
    st.markdown("**Visão de detalhada dos dados**", unsafe_allow_html=True)
    st.dataframe(df2)
