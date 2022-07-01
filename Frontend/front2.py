from copyreg import dispatch_table
from re import S
import string
from tkinter import Image
from tkinter.tix import IMAGETEXT
from turtle import color
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

#with open("style.css") as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

placeholder = st.empty()
with placeholder.container():

    pag1,pag2,pag3 = st.columns(3)

    pag1.button('Clicka 1')
    pag2.button('Clicka 2')
    pag3.button('Clicka 3')

    if pag1:
        st.write("pagina 1 :tumbsup:")
    elif pag2:
        st.write("pagina 2222222 :tumbsup:")
    elif pag3:
        st.write("pagina 32")
