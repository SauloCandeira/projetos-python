 import dash
import dash_core_components as dcc
import dash_html_components as html
from random import random
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pyodbc 
import dash_table
global data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, 'https://use.fontawesome.com/releases/v5.9.0/css/all.css'])

#server = '10.****' 
#database = '****' 
#username = '***' 
#password = '***' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')

def connectSQLServer(conn):
    connSQLServer = conn
    return connSQLServer

sql_query = ('''
                     SELECT * FROM impressoras
                '''
            )

df = pd.read_sql(sql_query,conn)
df.to_excel("FileExample.xlsx",sheet_name='Results')
print(df)



#------------------------ Filtro de Dados
nome_impressora = df.loc[:,"nome"]
#data_carga = df.loc[:,"dt"]
tonner = df.loc[:,"tonner"]


#------------------------ Graficos
figura = plt.figure(figsize=(10,3))
#figura.suptitle()
plt.plot(nome,tonner)
plt.legend()
plt.show()