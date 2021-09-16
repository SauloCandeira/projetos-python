

#--------------- SELECT
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
def connectSQLServer(conn):
    connSQLServer = conn
    return connSQLServer
sql_query = ('''SELECT * FROM impressoras ORDER BY tonner''')

#--------------- INSERT

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
cursor = conn.cursor()
string_sql = f'''INSERT INTO impressoras VALUES ('{coluna['value']}', '{nome}', '{ip}', '{andar}', '{sala}', '{setor}', '{total_impressao}', '{total_scan}', '{total_cilindro}', '{dt}')'''
cursor.execute(string_sql)
conn.commit()

#--------------- UPDATE

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
cursor = conn.cursor()
string_sql = f'''INSERT INTO impressoras VALUES ('{coluna['value']}', '{nome}', '{ip}', '{andar}', '{sala}', '{setor}', '{total_impressao}', '{total_scan}', '{total_cilindro}', '{dt}')'''
cursor.execute(string_sql)
conn.commit()