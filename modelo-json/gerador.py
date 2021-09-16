import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import json



# BASE DE DADOS I
receitas = 'teste/servidores.json'
df_dia_1 = pd.read_json(receitas)
#df_dia_1 = json.loads(receitas)

# BASE DE DADOS 2
#depesas = 'Liquidado.xlsx'
#df_dia_2 = pd.read_csv(arquivo_excel_2)

# UNIR BASE DE DADOS
#relatorio = pd.concat([df_dia_1], axis=1)
#relatorio = pd.concat([df_dia_1,df_dia_2], axis=1)
#relatorio = pd.concat([df_dia_1,df_dia_2])
#print(relatorio)

#print(df_dia_1)['cpf'])

# MODELAGEM DE DADOS
#relatorio2 = relatorio.groupby(['Valor']).sum()
#print(relatorio2)

#relatorio_bonito = relatorio.loc[:,"nome"]
#print(relatorio_bonito)
#print(relatorio2)
#print(df_dia_1.loc["data"])

# GERAR GRAFICOS
#relatorio_bonito.plot(kind="bar")

#for user in users:
#    print(df_dia_1["nome"])

#plt.show()
