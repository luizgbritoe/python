import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "122026"
)

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS meu_banco")

cursor.execute("USE meu_banco")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoal (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
        )""")

print("Banco e tabela criados com sucesso!")