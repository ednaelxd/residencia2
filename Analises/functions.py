import pandas as pd
import glob

def concatenador(path):
    path = path
    filenames = glob.glob(path + "/*.csv")

    li= []

    for filename in filenames:
        df = pd.read_csv(filename, index_col=None, header=0, encoding='latin-1',sep=';',decimal=',')
        li.append(df)

    df2 = pd.concat(li, axis=0, ignore_index=True)
    
    return (df2)


#varre todos o objetos e identifica se possui relacao com obras
#Define como obra ou nao
def eh_obra(x):
    y=[]
    if ('OBRAS' in x) or ('OBRA' in x) or ('ENGENHARIA' in x) or
    ('engenharia' in x) or ('obras' in x) or ('obra' in x) or
    ('CONTRU-CAO' in x) or ('constru-cao' in x):
        y.append('OBRAS')
    else:
        y.append('COMPRA/SERVIÇOS')
    y=y.pop(0)
    return(y)

#aplica a função de descobrimento de obras de forma mais rápida no dataframe
def separaObra(df2):
    return pd.Series(eh_obra(row.Objeto)
        for row in df2.itertuples()
  )