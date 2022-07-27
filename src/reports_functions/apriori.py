import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def apriori_generator(df):
    #separando dataset
    df_o = df[df['Tipo']=='Obras']
    df_c = df[df['Tipo']=='Compras/Servicos']

    #contagens
    count_per_trans1 =df_o.groupby(['Número Licitação','Descrição'])['Descrição'].count().reset_index(name='Count')
    count_per_trans2 =df_c.groupby(['Número Licitação','Descrição'])['Descrição'].count().reset_index(name='Count')

    #pivot tables
    Item_based_matrix1 = count_per_trans1.pivot_table(index='Número Licitação', columns='Descrição', values='Count', aggfunc='sum').fillna(0)
    Item_based_matrix2 = count_per_trans2.pivot_table(index='Número Licitação', columns='Descrição', values='Count', aggfunc='sum').fillna(0)

    #binarização
    # Convert entries as 0 and 1
    def encode(x):
        if x <=0:
            return 0

        elif x >=1:
            return 1

    # apply the function
    Item_based_matrix1 = Item_based_matrix1.applymap(encode)
    Item_based_matrix2 = Item_based_matrix2.applymap(encode)

    #apriori run
    frequent_itemsets1 = apriori(Item_based_matrix1, min_support = 0.05, use_colnames = True)
    frequent_itemsets2 = apriori(Item_based_matrix2, min_support = 0.05, use_colnames = True)

    rules1 = association_rules(frequent_itemsets1, metric="confidence", min_threshold=0.7)
    obras_fim = rules1.sort_values('support').head(20)

    rules2 = association_rules(frequent_itemsets2, metric="confidence", min_threshold=0.7)
    serv_fim = rules2.sort_values('support').head(20)

    obras_fim['antecedents'] = obras_fim['antecedents'].apply(lambda x: list(x)[0])
    obras_fim['consequents'] = obras_fim['consequents'].apply(lambda x: list(x)[0])
    print('deu certo1')
    serv_fim['antecedents'] = serv_fim['antecedents'].apply(lambda x: list(x)[0])
    serv_fim['consequents'] = serv_fim['consequents'].apply(lambda x: list(x)[0])
    print('deu certo2')
    return(obras_fim,serv_fim)


