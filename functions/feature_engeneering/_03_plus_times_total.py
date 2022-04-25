import numpy as np

def calcula_pct_teto(data):
    
    # Inicialização
    data = np.array(data)
    pct_teto = []
    ###############
    for linhas in data:
        
        if linhas[-1] == 0:
            #print(linhas)
            #TAG'AMENTO DAS LICITACOES DDO TIPO: REGISTRO DE PRECO
            if (linhas[4]=='Pregão - Registro de Preço' or linhas[4]=='Concorrência - Registro de Preço' or linhas[4]=='Concorrência') and (linhas[-2]=='Obras'):
                pct_teto.append(linhas[-3] / 3300000)

            if (linhas[4]=='Pregão - Registro de Preço') and (linhas[-2]=='Compras/Servicos'):
                pct_teto.append(linhas[-3] / 1430000)

            #TAG'AMENTO DAS LICITACOES DO TIPO: DISPENSA LICITACAO
            if (linhas[4]=='Dispensa de Licitação') and (linhas[-2]=='Obras'):
                pct_teto.append(linhas[-3] / 33000)
            if (linhas[4]=='Dispensa de Licitação')  and (linhas[-2]=='Compras/Servicos'):
                pct_teto.append(linhas[-3] / 17600)

            #TAG'AMENTO DAS LICITACOES DO TIPO: TOMADA DE PREÇOS
            if (linhas[4]=='Tomada de Preços')  and (linhas[-2]=='Obras'):
                pct_teto.append(linhas[-3] / 3300000)                          
            if (linhas[4]=='Tomada de Preços')  and (linhas[-2]=='Compras/Servicos'):
                pct_teto.append(linhas[-3] / 1400000)

            #TAG'AMENTO DAS LICITACOES DO TIPO: CONVITE
            if (linhas[4]=='Convite')  and (linhas[-2]=='Obras'):
                pct_teto.append(linhas[-3] / 176000)
            if (linhas[4]=='Convite')   and (linhas[-2]=='Compras/Servicos'):
                pct_teto.append(linhas[-3] / 330000)

    return(pct_teto)