import pandas as pd
import numpy as np 
import glob

#DEFININDO FUNçÕES 

def importa_dados_participantes(url): 
    
    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url)
    
    # Deletando/criando coluna desnecessaria
    df.drop(columns=['Unnamed: 0','Nome UG', 'Modalidade Compra','Nome Órgão','Código Item Compra','Código UG', 'Código Modalidade Compra', 'Código Órgão'], axis=1, inplace=True)
    
    return (df)

def importa_dados_taguiados():
    # importando os dados do framework_00
    from framework_00 import df
    df_tag = df
    
    # Deletando/criando coluna desnecessaria
    df_tag.drop(columns=['Nome UG','Modalidade Compra','Objeto','Situação Licitação','Código Órgão Superior','Nome Órgão Superior','Código Órgão','Município','data','Data Abertura','Total','Obras','Código Modalidade Compra','Código UG'], axis=1, inplace=True)
    
    return (df_tag)

def merge_dados_taguiados(df_part , df_tag):
    # Aplicando o merge nos dataframes
    m = pd.merge(df_tag, df, how = 'inner', on = ('Número Processo','Número Licitação'))
    
    # Retirando dados nulos
    m = m.dropna()
    
    # criando dataframe com os dados fraudulentos
    df_0 = m[m["Tag"]==0] 
    
    return (m, df_0)

def analise_exploratória(df_0):
    # Número de participantes
    n_part = len(df_0["CNPJ Participante"].unique())
    
    # Número de empresas vencedoras
    n_venc = len(df_0[df_0["Flag Vencedor"]== "SIM"]["CNPJ Participante"].unique())
    
    # Número de processos e licitações fraudulentas
    n_proc = len(df_0["Número Processo"].unique())
    n_lic = len(df_0["Número Licitação"].unique())
    
    # Número de itens diferentes
    n_itens = len(df_0["Descrição Item Compra"].unique())
    
    #Printando os resultados
    print("\nNúmero de Empresas Participantes em Processos Fraudulentos: ", n_part,
          "\nNúmero de Empresas Vencedoras de Processos Fraudulentos: ", n_venc,
          "\nNúmero de Processos Fraudulentos: ",n_proc,
          "\nNúmero de Licitações Fraudulentas: ",n_lic,
          "\nNúmero de Itens Fraudulentos: ", n_itens)
    #n_part, n_venc, n_proc, n_lic, n_itens
    return ()

def list_part_itens(df_0):
    # Participantes com maior número de participações em licitações fraudulentas
    print("\nParticipantes com maior número de participações em licitações fraudulentas: \n")
    print(df_0.loc[:,["CNPJ Participante" , "Nome Participante"]].value_counts().head(10))
    
    # Participantes com maior número de vitórias em licitações fraudulentas
    print("\n\nParticipantes com maior número de vitórias em licitações fraudulentas: \n")
    print(df_0[df_0["Flag Vencedor"]== 'SIM'].loc[:,["CNPJ Participante" , "Nome Participante"]].value_counts().head(10))
    
    # Itens com maior número de aparições em licitações fraudulentas
    print("\n\nItens com maior número de aparições em licitações fraudulentas: \n")
    print(df_0[df_0["Flag Vencedor"]== 'SIM'].loc[:,["Descrição Item Compra"]].value_counts().head(10))
    
    # Orgão com maior número de processos fraudulentos
    print("\n\nOrgão com maior número de processos fraudulentos: \n")
    print(df_0[df_0["Flag Vencedor"]== 'SIM'].loc[:,["Nome Órgão"]].value_counts().head(10))

#COMEÇANDO O PROGRAMA 

df_tag = importa_dados_taguiados()

###############################
#print("Modelo da URL: C:\Users\gabri\Desktop\Data\dados_participantes_.csv")
url = input("Digite a URL do Dados dos Participantes: ")
###############################
print("....... Importando os dados .......")
df = importa_dados_participantes(url)

print("\n....... Mesclando os dataframes .......")
m , df_0 = merge_dados_taguiados(df , df_tag)

print("\n....... Printando análises .......\n")
analise_exploratória(df_0)
list_part_itens(df_0)
