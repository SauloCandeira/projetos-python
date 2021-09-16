import dash
from dash.development.base_component import Component
from dash.html.H3 import H3
from dash.html.Span import Span
from dash_bootstrap_components._components.Card import Card
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import pyodbc 
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

############################# BANCO DE DADOS
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
def connectSQLServer(conn):
    connSQLServer = conn
    return connSQLServer
sql_query = (''' SELECT nome, tonner, dt FROM impressoras_graficos ORDER BY tonner ''')
df = pd.read_sql(sql_query,conn)
#df.to_excel("FileExample.xlsx",sheet_name='Results')
print(df)

############################# GRAFICOS
fig = px.bar(df, x=(df["nome"]), y=(df["tonner"]), barmode="group")


############################# LAYOUT
app.layout = html.Div(children=[

    # ------------------- TITULO
    html.H2(children='Controladoria Geral do Distrito Federal - CGDF'),

    # ------------------- DESCRIÇÃO I
    html.Div(children='''Sistema de monitoramento de impressoras'''),

    # ------------------- CARDS
   
       
    dbc.Card ([
        html.Span('ONLINE:'),
        html.H3(style={"color": "#adfc92"})
    ]), 
    dbc.Card ([
        html.Span('OFFLINE:'),
        html.H3(style={"color": "#adfc92"})
    ]), 
       

    
    # ------------------- DESCRIÇÃO II
    html.H3(id= 'text', children='Buscar por:'),

    # ------------------- MENU DROPDOWN
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Imp-on', 'value': 'IMP-ON'},
            {'label': 'Imp-off', 'value': 'IMP-OFF'}
        ],
        value='ALL'
    ),

    # ------------------- GRAFICO I
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)


def changeText(value):
    if value == 'ALL':
        return px.bar(df, x=(df["nome"]), y=(df["tonner"]), barmode="group")
    elif value == 'IMP-ON':
        return px.bar(df[df['dt'] == '2021-09-16'], x=(df["nome"]),  y=(df["tonner"]), barmode="group")
#    else:
#        return px.bar(df[df['City'] == 'SF'], x="Fruit", y="Amount", color="City", barmode="group")    
#   
    return 
    

if __name__ == '__main__':
    app.run_server(debug=True)