import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

#__START_____________________
print('. . . . . Importando dados lict . . . . .\n')
from functions.feature_engeneering._00_import_merge import importa_dados_zip, importa_dados_participantes, merge_dados_taguiados

city = pd.read_csv('C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\cidades.csv')
df = importa_dados_zip('C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\data_all.zip')
#__END_______________________

#__START_____________________
print('. . . . . . .Adc Coluna Obras . . . . . .\n')
from functions.feature_engeneering._01_obra_or_notobra import define_obra

df['Obras'] = define_obra(df)
df['Tag'] = 0
#__END_______________________

#__START_____________________
print(df.head())
print(df['Obras'].value_counts())
print(df.shape)
print('. . . . . . .TAGUIANDO . . . . . .\n')
from functions.feature_engeneering._02_classification import classificador

df['Tag'] = classificador(np.array(df))
#__END_______________________


print('. . . . . . .Importando base participantes . . . . . .\n')
df_part = importa_dados_participantes('C:\\Users\\efvs\\Documents\\Residencia Ednael\\Repositórios\\dados_participantes.zip')

print('. . .Concatenando Informações part. . . .\n')
merge1 = merge_dados_taguiados(df,df_part,('Número Processo','Número Licitação'))

print('. . . .  . Adicionando Cidades. . . . . .\n')
df_final = merge_dados_taguiados(merge1,city,('Município'))

df_final.to_csv('df_geral.csv')
del(merge1,df_final,df)