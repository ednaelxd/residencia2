import pandas as pd

def indice_fraude_estado(dados,data_inicio,data_final):
    colunas = ['{%} de Ilegalidades','Total de Licitações','Total de Ilegais','Valor Licitado','Valor Ilegal','{%} Valor Ilegal']
    print("Para o perído de {} à {}".format(data_inicio,data_final))
    #print("________________")
    percentagem = (dados['UF'][(dados['Tag']==0) & (dados['data']>=data_inicio) & (dados['data']<=data_final)].value_counts()/dados['UF'][(dados['data']>=data_inicio) & (dados['data']<=data_final)].value_counts()).sort_values(ascending=False)
    total_ileg = dados['UF'][(dados['Tag']==0) & (dados['data']>=data_inicio) & (dados['data']<=data_final)].value_counts()
    total = dados['UF'][(dados['data']>=data_inicio) & (dados['data']<=data_final)].value_counts()


    results = pd.merge(percentagem,total,how = 'inner', left_index=True, right_index=True)
    results = pd.merge(results,total_ileg,how = 'inner',left_index=True, right_index=True)

    valor_licitado = dados.groupby(['UF']).agg({'Total':'sum'})
    valor_licitado = valor_licitado['Total']
    valor_ilegal = dados[dados['Tag']==0].groupby(['UF']).agg({'Total':'sum'})
    valor_ilegal= valor_ilegal['Total']
    pct_valor_ileg = valor_ilegal/valor_licitado

    results = pd.merge(results,valor_licitado,how = 'inner',left_index=True, right_index=True)
    results = pd.merge(results,valor_ilegal,how = 'inner',left_index=True, right_index=True)
    results = pd.merge(results,pct_valor_ileg,how = 'inner',left_index=True, right_index=True)

    results.columns = colunas

    return(results)