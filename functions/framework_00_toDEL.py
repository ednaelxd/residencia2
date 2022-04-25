import pandas as pd
import numpy as np

'''print('. . . . . Importando dados . . . . .\n')
def importa_dados_zip(url):
    
    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url,compression='zip')
    
    # Deletando/criando coluna desnecessaria
    del(df['Unnamed: 0'])
    
    # Ajustando nomes
    df.rename(columns={'Data Resultado Compra':'data'},inplace=True)
    
    return (df)'''

############################
print('EXEMPLO: C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\data_all.zip')
url = input('Digite o endereço do arquivo zip no seu pc: ')
df = importa_dados_zip(url)
#df = importa_dados_zip(r'C:\Users\efvs\Documents\Residencia Ednael\Repositórios\data_all.zip')
############################

print('. . . . . Rotulando Obras . . . . .')
'''def define_obra(data):
    
    result = data.Objeto.str.contains("OBRAS|OBRA|obras|obra|ENGENHARIA|engenharia|CONSTRU-CAO|constru-cao", na=False)
    
    return (result.replace({True:'Obra',False:'Compras/Servicos'}))
'''
############################
df['Obras'] = define_obra(df)
df['Tag'] = 0
############################


'''print('. . . . . Taguiando os dados . . . . .')
def classificador(aa):
    
    #dados no formato Numpy
    
    for linhas in aa:

        #TAG'AMENTO DAS LICITACOES DDO TIPO: REGISTRO DE PRECO
        if (linhas[4]=='Pregão - Registro de Preço' or linhas[4]=='Concorrência - Registro de Preço' or linhas[4]=='Concorrência')  and linhas[-3]>3300000 and linhas[-2]=='Obras':
            linhas[-1] = 1 #EH LEGAL
        if(linhas[4]=='Pregão - Registro de Preço')  and (linhas[-3] > 1430000) and (linhas[-2]=='Compras/Servicos'):
            linhas[-1] = 1 #EH LEGAL
            
            
        #TAG'AMENTO DAS LICITACOES DO TIPO: DISPENSA LICITACAO
        if(linhas[4]=='Dispensa de Licitação')  and (linhas[-3] <= 33000) and (linhas[-2]=='Obras'):
            linhas[-1] = 1 #EH LEGAL
        if(linhas[4]=='Dispensa de Licitação')  and (linhas[-3] <= 17600) and (linhas[-2]=='Compras/Servicos'):
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
    
    return(aa)'''


'''
    Funcionalidade 1: Display do Percentual de Licitações com irregularidade
'''

##########################
col_names = df.columns
df=pd.DataFrame(classificador(np.array(df)),columns=col_names)
##########################

print('\n\n')
print('Estrutura Final dos dados')
print(df.head())
print('\n\n')
print('Distribuição percentual da legalidade das licitações')
print(df['Tag'].value_counts()/df.shape[0])
