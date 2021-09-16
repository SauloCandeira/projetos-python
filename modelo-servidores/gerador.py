import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 
import json


####| PARTE I - RASTREAR DADOS |####
url = 'https://portaldatransparencia.cgu.gov.br/servidores/consulta/resultado?paginacaoSimples=false&tamanhoPagina=2000000&offset=30&direcaoOrdenacao=asc&colunaOrdenacao=nome&colunasSelecionadas=detalhar%2Ctipo%2Ccpf%2Cnome%2CorgaoServidorLotacao%2Cmatricula%2Csituacao%2Cfuncao%2Ccargo%2Cquantidade&t=0nI7yachtEr4pENBm5FE&_=1629746872044'
arquivo_json = pd.read_json(url)
base_dados = arquivo_json["data"]

####|  PARTE II - LOCALIZAR ITENS |#####
lista_empenho = []

for conteudo in base_dados:  

    cpf = conteudo['cpf']
    nome = conteudo['nome']
    cargo = conteudo['cargo']
    orgaoServidorLotacao = conteudo['orgaoServidorLotacao']



    if conteudo['orgaoServidorLotacao'].strip() == 'Departamento de Polícia Federal':
        #empenhado = conteudo['orgaoVinculado']
        print('cpf', ': ',cpf)
        print('nome', ': ',nome)
        print('cargo', ': ',cargo)
        print('orgaoServidorLotacao', ': ',orgaoServidorLotacao)
    print( )


####|  GERAR GRAFICOS |#####

#relatorio_bonito.plot(kind="bar")

#for user in users:
#    print(df_dia_1["nome"])

#plt.show()

####|  PARTE III - CONEXÃO BANCO DE DADOS |#####
