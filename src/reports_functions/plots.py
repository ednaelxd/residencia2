# BARPLOTS - INDICES ESTADUAIS

import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px


def plot_bar_valores(df,tipo):
    
    if tipo == 1:

        fig = make_subplots(rows=2, cols=1,#,specs=[[{}, {}],
           #[{"colspan": 2}, None]],
           subplot_titles=("Montante Irregular por estado","índice de Prejuízo"))       

        df=df.sort_values(by='Valor Ilegal',ascending=False)
        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        indexes=df.index

        fig.add_trace(go.Bar(name=df.columns[3],
                x=indexes, y=df['Valor Ilegal'],
                text=(df['Valor Ilegal']/1000000).round(2),
                textposition='auto'    
        ),row=1,col=1).update_yaxes(tickprefix="R$",row=1,col=1)
        
        df = df.sort_values(by='{%} Valor Ilegal',ascending=False)

        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        indexes=df.index

        fig.add_trace(go.Bar(name=df.columns[5], 
                x=indexes, y=df['{%} Valor Ilegal'],
                text=(df['{%} Valor Ilegal']*100).round(2),
                textposition='auto'        
            ),row=2,col=1).update_yaxes(tickformat='.2%',row=2,col=1)

        return(fig)

    if tipo == 2:


        fig = make_subplots(rows=2, cols=1,#,specs=[[{}, {}],
           #[{"colspan": 2}, None]],
           subplot_titles=("Quantidade de licitações irregulares","Índice de Irregularidade"))       


        df=df.sort_values(by='Total de Licitações',ascending=False)
        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        #indexes=df_bal.index
        indexes = df.index
        #Geral##

        fig.add_trace(go.Bar(name=df.columns[2], 
                x=indexes, y=df['Total de Ilegais'].values,
                text=df['Total de Ilegais'],
                textposition='outside'        
            ),row=1,col=1)

        df2 = df.sort_values(by='{%} de Ilegalidades',ascending=False)

        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df2['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        indexes=df.index

        fig.add_trace(go.Bar(name=df.columns[0], 
           x=indexes, y=df['{%} de Ilegalidades'].values,
           text=(df['{%} de Ilegalidades']*100).round(2),
           textposition='outside'        
       ),row=2,col=1).update_yaxes(tickformat='.2%',row=2,col=1)

        return(fig)
    

# TOPITENS

def plota_treemap_itens(dd,ini,fim):

        #dd1=dd[dd['Tag']==1]
        dd2=dd[(dd['Tag']==0) & (dd['data']>=ini) & (dd['data']<=fim)]

        dd3=dd2['Total']/1000000

        fig = px.treemap(dict(dd2),path=[px.Constant('Estados'),dd2['UF'],'Nome Órgão Superior'],#,dd2['Objeto'].values],
                        values=dd3,maxdepth=3)
        #           values='Total de Licitações')
        fig.update_layout(uniformtext_minsize=18)
        fig.update_traces(root_color="lightgray",textfont_color='rgb(255,255,255)')

        fig.update_layout(
        title_text='Itens por Estado-Órgão, em licitações Irregulares',title_x=0.5
                        )
        fig.update_layout(margin = dict(t=70, l=25, r=25, b=25))
        fig.data[0].customdata = dd3
        fig.data[0].texttemplate = "%{label}<br>Totais: R$%{value:.2f}M"
        fig.data[0]['textfont']['size']=13
        return(fig)

# EXIBIÇÃO DOS TOP-PLUS TOTAL

def plot_plus_total(df):

    dd3=df.sort_values(by='pct_do_teto',ascending=False)

    fig = px.bar(dd3[0:20],x=('Número Processo'),
                    y='pct_do_teto',hover_data=['Município','Nome Órgão Superior'],color='UF')
    #           values='Total de Licitações')
    #fig.update_layout(uniformtext_minsize=14)
    #fig.update_traces(root_color="lightgrey")
    fig.update_layout(
        title_text='Top 20: Licitações que mais ultrapassam o teto estabelecido pro Lei'
    )
    return(fig)

# EXIBIÇÃO DOS TOP OBJETCOTS
def plot_lista_objetos(gp2):
    gp3=gp2.copy()
    cont=0
    for line in gp3['Objeto']:
        gp3['Objeto'][cont] = line[0:30] +'<br>'+line[30:]
        cont+=1
        #print('entrou aq')
    fig = px.treemap(gp3,path=['UF','Objeto'],values='count',
                maxdepth=3)
    fig.data[0]['textfont']['size']=13
    return(fig)

def plot_tops(df):
    fig = px.bar(df,x=df.iloc[:,1],y=df.iloc[:,0])
    return(fig)

# EXIBIÇÃO DOS TOP-PARTICIPANTES