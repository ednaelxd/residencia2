import pandas as pd
import numpy as np
###
from src.feature_engeneering._00_import_merge import importa_dados_zip, importa_dados_participantes, merge_dados_taguiados

def generate_1(url_data,url_citys):
    print('url_data =','C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\cidades.csv')
    print('url_cidades =','C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\cidades.csv')
    #__START_____________________
    print('. . . . . Importando dados lict . . . . .\n')
    city = pd.read_csv(url_citys, index_col=[0])
    df = importa_dados_zip(url_data)
    #__END_______________________

    #__START_____________________
    print('. . . . . . .Adc Coluna Obras . . . . . .\n')
    from src.feature_engeneering._01_obra_or_notobra import define_obra
    df['Obras'] = define_obra(df)
    df['Tag'] = 0
    #__END_______________________

    #__START_____________________
    print('. . . . . . .TAGUIANDO . . . . . .\n')
    from src.feature_engeneering._02_classification import classificador
    df['Tag'] = classificador(np.array(df))
    #__END_______________________

    print('. . . .  . Adicionando Cidades. . . . . .\n')
    df_final = merge_dados_taguiados(df,city,('Município'))

    return(df_final)
'''
print('. . . . . . .Importando base participantes . . . . . .\n')
df_part = importa_dados_participantes('C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\dados_participantes.zip')

print('. . .Concatenando Informações part. . . .\n')
merge1 = merge_dados_taguiados(df,df_part,('Número Processo'))
'''
