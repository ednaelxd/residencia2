import numpy as np

def classificador(aa):
    
    #dados no formato Numpy
    
    for linhas in aa:

        #TAG'AMENTO DAS LICITACOES DDO TIPO: REGISTRO DE PRECO
        if (linhas[4]=='Pregão - Registro de Preço' or linhas[4]=='Concorrência - Registro de Preço' or linhas[4]=='Concorrência')  and linhas[-3]>3300000 and linhas[-2]=='Obras':
            linhas[-1] = 1 #EH LEGAL
        if(linhas[4]=='Pregão - Registro de Preço')  and (linhas[-3] > 1430000) and (linhas[-2]=='Compras/Servicos'):
            linhas[-1] = 1 #EH LEGAL
            
            
        #TAG'AMENTO DAS LICITACOES DO TIPO: DISPENSA LICITACAO
        if(linhas[4]=='Dispensa de Licitação')  and (linhas[-3] <= 100000) and (linhas[-2]=='Obras'):
            linhas[-1] = 1 #EH LEGAL
        if(linhas[4]=='Dispensa de Licitação')  and (linhas[-3] <= 50000) and (linhas[-2]=='Compras/Servicos'):
            linhas[-1] = 1 #EH LEGAL
            
            
        #TAG'AMENTO DAS LICITACOES DO TIPO: TOMADA DE PREÇOS
        if(linhas[4]=='Tomada de Preços')  and (linhas[-3] > 330000 and linhas[-3] <= 3300000) and (linhas[-2]=='Obras'):
            linhas[-1] = 1
        if(linhas[4]=='Tomada de Preços')  and (linhas[-3] > 176000 and linhas[-3] <= 1400000) and (linhas[-2]=='Compras/Servicos'):
            linhas[-1] = 1 #EH LEGAL
            
        #TAG'AMENTO DAS LICITACOES DO TIPO: CONVITE
        if(linhas[4]=='Convite')  and (linhas[-3] > 17600 and linhas[-3] <= 176000) and (linhas[-2]=='Obras'):
            linhas[-1] = 1 #EH LEGAL
        if(linhas[4]=='Convite')  and (linhas[-3] > 33000 and linhas[-3] <= 330000) and (linhas[-2]=='Compras/Servicos'):
            linhas[-1] = 1 #EH LEGAL
            
        #TAG'AMENTO DAS LICITACOES DO TIPO: PREGÃO | INEXIGIBILIDADE DE LICITAÇÃO | CONCURSO | CONCORRENCIA INTERNACIONAL
        if(linhas[4]=='Pregão' or linhas[4]=='Inexigibilidade de Licitação' or linhas[4]=='Concurso' or linhas[4]=='Concorrência Internacional'):
            linhas[-1]=1 #EH LEGAL
    tags = aa[:,-1]
    
    return(tags)