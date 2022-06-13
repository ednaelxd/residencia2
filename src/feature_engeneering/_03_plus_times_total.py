import numpy as np

def calcula_pct_teto(data):
    
    #Inicialização
    #data2 = data.copy()
    #data2['pct'] = 0
    data = np.array(data)
    lista_zerada = [0]
    pct_teto=[]
    #pct_teto = lista_zerada*data.shape[0]
    ###############
    cont=0

    for linhas in data:     

        #pct_teto=0
        if linhas[-2] == 0:
            #TAG'AMENTO DAS LICITACOES DDO TIPO: REGISTRO DE PRECO
            if ((linhas[4]=='Pregão - Registro de Preço' or linhas[4]=='Concorrência - Registro de Preço' or linhas[4]=='Concorrência') and (linhas[-3]=='Obra')):
                pct_teto.append(linhas[-4] / 3300000)
                #print(cont, "entrou aq")
            elif ((linhas[4]=='Pregão - Registro de Preço') and (linhas[-3]=='Compras/Servicos')):
                pct_teto.append(linhas[-4] / 1430000)
                #print(cont, "entrou aq")
            #TAG'AMENTO DAS LICITACOES DO TIPO: DISPENSA LICITACAO
            elif ((linhas[4]=='Dispensa de Licitação') and (linhas[-3]=='Obra')):
                pct_teto.append(linhas[-4] / 33000)
                ##print(cont, "entrou aq")

            elif ((linhas[4]=='Dispensa de Licitação')  and (linhas[-3]=='Compras/Servicos')):
                pct_teto.append(linhas[-4] / 17600)
                #print(cont, "entrou aq")

            #TAG'AMENTO DAS LICITACOES DO TIPO: TOMADA DE PREÇOS
            elif ((linhas[4]=='Tomada de Preços')  and (linhas[-3]=='Obra')):
                pct_teto.append(linhas[-4] / 3300000)
                #print(cont, "entrou aq")

            elif ((linhas[4]=='Tomada de Preços')  and (linhas[-3]=='Compras/Servicos')):
                pct_teto.append(linhas[-4] / 1400000)
                #print(cont, "entrou aq")

            #TAG'AMENTO DAS LICITACOES DO TIPO: CONVITE
            elif ((linhas[4]=='Convite')  and (linhas[-3]=='Obra')):
                pct_teto.append(linhas[-4] / 176000)
                #print(cont, "entrou aq")

            elif ((linhas[4]=='Convite')   and (linhas[-3]=='Compras/Servicos')):
                pct_teto.append(linhas[-4] / 330000)
                #print(cont, "entrou aq")
                
        #data2.iloc[cont,-1]=pct_teto
        cont+=1
    return(pct_teto)