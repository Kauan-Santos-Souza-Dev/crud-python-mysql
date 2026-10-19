# Instalar o mysql-connector-python "pip install mysql-connector-python"
# Esconder Senhas: pip install python-dotenv
import os
import mysql.connector
from dotenv import load_dotenv

# dotenv (python-dotenv): é a biblioteca que você instalou com o pip. 
# Ela sabe ler o arquivo .env. O Python, sozinho, não sabe que esse arquivo existe: para ele é só mais um arquivo de texto na pasta.

load_dotenv()
# load_dotenv(): é a função dessa biblioteca que faz a leitura.

# Configurando para conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
# Verificar se Conectou 

# print("Conectado!" if conexao.is_connected() else "Falhou")
# conexao.close()

# Iniciando o cursor para executar comandos SQL
cursor = conexao.cursor() 

# CREATE 
nome_Produto = "toddynho"
valor = 3

comando = 'INSERT INTO vendas (nome_Produto, valor) VALUES (%s, %s)' # Fazer um comando SQL
cursor.execute(comando, (nome_Produto, valor)) # Executar o comando SQL
conexao.commit() # edita o banco de dados

# READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando) # Executar o comando SQL
resultado = cursor.fetchall() # ler o banco de dados
print(resultado) # printar o resultado do banco de dados    

# UPDATE
idVendas = 3
valor = 4
comando = 'UPDATE vendas SET valor = %s WHERE idVendas = %s' # Fazer um comando SQL
cursor.execute(comando, (valor, idVendas))
conexao.commit()

# DELETE
idVendas = 2
comando = 'DELETE FROM vendas WHERE idVendas = %s' # Fazer um comando SQL
cursor.execute(comando, (idVendas,))
conexao.commit()

# Encerrando Cursor
cursor.close()
# Encerrando Conexão
conexao.close()