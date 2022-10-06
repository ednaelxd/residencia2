import pandas as pd

def importa_dados_zip(url):
    
    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url, index_col=[0])
    
    # Ajustando nomes
    df.rename(columns={'Data Resultado Compra':'data'},inplace=True)
    df['data']=pd.to_datetime(df['data'])
    return (df)

def importa_dados_participantes(url): 
    #Para reducao de tamanho do dado
    dtypes = {'Número Processo':'category',
          'Descrição Item Compra':'category',
          'CNPJ Participante':'category',
          'Nome Participante':'category',
          'Flag Vencedor':'category'}

    # url = link para o local onde os dados estão armazenados
    df = pd.read_csv(url,compression='zip',dtype=dtypes)
    
    # Deletando/criando coluna desnecessaria
    df.drop(columns=['Unnamed: 0','Nome UG', 'Modalidade Compra','Nome Órgão','Código Item Compra','Código UG', 'Código Modalidade Compra', 'Código Órgão'], axis=1, inplace=True)
    
    return (df)

def merge_dados_taguiados(df_part , df_tag, tupla_merge):
    # Aplicando o merge nos dataframes
    m = pd.merge(df_part, df_tag, how = 'inner', on = tupla_merge)
    
    # Retirando dados nulos
    m = m.dropna()
    
    return (m)