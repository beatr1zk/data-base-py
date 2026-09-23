import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Bia@2008ksql",
        database = "ifood2"
    )
    return conexao