import pyodbc
from properties import getConfigSection

properties = getConfigSection('DATABASE')

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                properties['server_name']+';DATABASE='+properties['db_name']+';UID='+properties['db_username']+';PWD='+properties['db_password'])
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
