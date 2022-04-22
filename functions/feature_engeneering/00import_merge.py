import pandas as pd

print('. . . . . Importando dados . . . . .\n')
def importa_dados_zip(url):
    
    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url,compression='zip')
    
    # Deletando/criando coluna desnecessaria
    del(df['Unnamed: 0'])
    
    # Ajustando nomes
    df.rename(columns={'Data Resultado Compra':'data'},inplace=True)
    
    return (df)

def importa_dados_participantes(url): 
    
    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url)
    
    # Deletando/criando coluna desnecessaria
    df.drop(columns=['Unnamed: 0','Nome UG', 'Modalidade Compra','Nome Órgão','Código Item Compra','Código UG', 'Código Modalidade Compra', 'Código Órgão'], axis=1, inplace=True)
    
    return (df)

def merge_dados_taguiados(df_part , df_tag):
    # Aplicando o merge nos dataframes
    m = pd.merge(df_tag, df, how = 'inner', on = ('Número Processo','Número Licitação'))
    
    # Retirando dados nulos
    m = m.dropna()
    
    # criando dataframe com os dados fraudulentos
    df_0 = m[m["Tag"]==0] 
    
    return (m, df_0)