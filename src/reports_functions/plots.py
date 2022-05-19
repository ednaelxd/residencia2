# DASHBOARD DOS RESULTADOS POR ESTADO

import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots


def plot_bar_valores(df,tipo):
    
    fig = make_subplots(rows=2, cols=2,specs=[[{}, {}],
           [{"colspan": 2}, None]])

    if tipo == 1:

        df=df.sort_values(by='Valor Licitado',ascending=False)
        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        df_bal=df.drop(['AC','SE','RJ'],axis=0)
        indexes=df_bal.index

        fig.add_trace(go.Scatter(name=df_bal.columns[3], x=indexes, 
                y=df_bal['Valor Licitado'].values,mode='lines+markers'
                ),2,1)
        fig.add_trace(go.Bar(name=df_bal.columns[4], 
                x=indexes, y=df_bal['Valor Ilegal'].values,
                text=df['{%} Valor Ilegal'],
                textposition='outside'        
            ),row=2,col=1)

        fig.add_trace(go.Scatter(name=df.columns[3], x=['SE','RJ'], 
                y=df['Valor Licitado'][['SE','RJ']].values,mode='lines+markers'
                ),1,1)
        fig.add_trace(go.Bar(name=df.columns[4], 
                x=['SE','RJ'], y=df['Valor Ilegal'][['SE','RJ']].values,
                text=df['{%} Valor Ilegal'][['SE','RJ']],
                textposition='outside'        
            ),row=1,col=1)

        fig.add_trace(go.Scatter(name=df.columns[3], x=['AC'], 
                y=df['Valor Licitado'][['AC']].values,mode='lines+markers'
                ),1,2)
        fig.add_trace(go.Bar(name=df.columns[4], 
                x=['AC'], y=df['Valor Ilegal'][['AC']].values,
                text=df['{%} Valor Ilegal'][['AC']],
                textposition='outside'        
            ),row=1,col=2)

        return(fig)

    if tipo == 2:

        df=df.sort_values(by='Total de Licitações',ascending=False)
        df['{%} Valor Ilegal']=df['{%} Valor Ilegal'].round(4)
        df['{%} de Ilegalidades']=df['{%} de Ilegalidades'].round(4)
        df_bal=df.drop(['AC','SE','RJ'],axis=0)
        indexes=df_bal.index

        fig.add_trace(go.Scatter(name=df.columns[1], x=indexes, 
                y=df['Total de Licitações'].values,mode='lines+markers'
                ),2,1)
        fig.add_trace(go.Bar(name=df.columns[2], 
                x=indexes, y=df['Total de Ilegais'].values,
                text=df['{%} de Ilegalidades'],
                textposition='outside'        
            ),row=2,col=1)

        fig.add_trace(go.Scatter(name=df.columns[1], x=['SE','RJ'], 
                y=df['Total de Licitações'][['SE','RJ']].values,mode='lines+markers'
                ),1,1)
        fig.add_trace(go.Bar(name=df.columns[2], 
                x=['SE','RJ'], y=df['Total de Ilegais'][['SE','RJ']].values,
                text=df['{%} de Ilegalidades'][['SE','RJ']],
                textposition='outside'        
            ),row=1,col=1)

        fig.add_trace(go.Scatter(name=df.columns[1], x=['AC'], 
                y=df['Total de Licitações'][['AC']].values,mode='lines+markers'
                ),1,2)
        fig.add_trace(go.Bar(name=df.columns[2], 
                x=['AC'], y=df['Total de Ilegais'][['AC']].values,
                text=df['{%} de Ilegalidades'][['AC']],
                textposition='outside'        
            ),row=1,col=2)
        # Change the bar mode
        #fig.update_layout(barmode='group')
        #fig.update_xaxes(rangeslider_visible=True)
        #fig.show()

        return(fig)
    

# BOXPLOT DOS TOP-ITENS E SEUS VALORES


# EXIBIÇÃO DOS TOP-WINNERS


# EXIBIÇÃO DOS TOP-PARTICIPANTES