import pandas as pd 
import numpy as np 
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt 
import pyodbc

# PARTE I - LER JSON
url = 'http://www.portaltransparencia.gov.br/despesas/orgao/resultado?paginacaoSimples=false&tamanhoPagina=1&offset=0&direcaoOrdenacao=asc&colunaOrdenacao=orgaoSuperior&de=01%2F01%2F2021&ate=31%2F08%2F2021&colunasSelecionadas=linkDetalhamento%2CmesAno%2CorgaoSuperior%2CorgaoVinculado%2CvalorDespesaEmpenhada%2CvalorDespesaLiquidada%2CvalorDespesaPaga%2CvalorRestoPago&_=1628798234307'
arquivo_json = pd.read_json(url)
base_dados = arquivo_json["data"]
#print(base_dados)


# PARTE II - FILTRAR JSON
for tabelas in base_dados:
    
    mesAno = tabelas['mesAno']
    orgao = tabelas['orgaoSuperior']
    valorDespesaEmpenhada = tabelas['valorDespesaEmpenhada']
    valorDespesaLiquidada = tabelas['valorDespesaLiquidada']
    valorDespesaPaga = tabelas['valorDespesaPaga']
    valorRestoPago = tabelas['valorRestoPago']

    print('mesAno: ', mesAno)
    print('orgaoSuperior: ', orgao)
    print('valorDespesaEmpenhada: ', valorDespesaEmpenhada)
    print('valorDespesaLiquidada: ', valorDespesaLiquidada)
    print('valorDespesaPaga: ', valorDespesaPaga)
    print('valorRestoPago: ', valorRestoPago)
    #print(dados, ':', tabelas[dados])
    print( )
    
    
    #---- Matplot Lib -------

    data = [mesAno]
    tickers = ["valorDespesaPaga","valorDespesaEmpenhada", "valorDespesaLiquidada", "valorRestoPago"]
    figura = plt.figure(figsize=(10,3))
    figura.suptitle(orgao)

    plt.plot(tickers,data)
    plt.legend()
    plt.show()




    #---- Modelos -------
    #plt.plot(dado_x,dado_y, linestyle=':', color='#611718', label='dados', lw=5.0, marker= 'p')
    #plt.scatter(dado_x,dado_y)
    #plt.bar(dado_x,dado_y)

    #---- Configs -------
    #plt.ylabel('Eixo Y')
    #plt.xlabel('Eixo X')
    #plt.title('Titulo do Grafico')
    #plt.legend()
   


#CONNECTION SQL ------------------------------- IMP 01
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
cursor = conn.cursor()
string_sql = f'''INSERT INTO despesas VALUES ({data}, {despesa})'''
cursor.execute(string_sql)
conn.commit()




# PARTE III - INTERFACE GRAFICA
#class TelaPython:
#    def __init__(self):
#        layout = [

#            [sg.button()]
#        ]
#        janela = sg.Window("Dados do usuario").layout(layout)
#        self.button, self.values = janela.Read()
    
#    def Iniciar(self):
#        print(self.values)

#tela = TelaPython()
#tela.iniciar()

#https://www.youtube.com/watch?v=FDU-D8ddTU4