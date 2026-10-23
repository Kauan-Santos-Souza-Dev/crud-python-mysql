# Instalar o mysql-connector-python "pip install mysql-connector-python"
# Esconder Senhas: pip install python-dotenv
# É um módulo que já vem com o Python e serve para conversar com o sistema operacional. Aqui você só usa uma coisa dele: os.getenv("NOME"), que lê uma variável de ambiente, 
# um valor guardado na memória do processo, fora do seu código. Se a variável não existir, devolve None.
import os
import mysql.connector
from dotenv import load_dotenv

# dotenv (python-dotenv): é a biblioteca que você instalou com o pip. 
# Ela sabe ler o arquivo .env. O Python, sozinho, não sabe que esse arquivo existe: para ele é só mais um arquivo de texto na pasta.

load_dotenv()
# load_dotenv(): é a função dessa biblioteca que faz a leitura.
    
# Configurando para conectar ao banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
 

# CREATE 
def criar_vendas(nome_Produto,valor):    
# Criar uma conexão com banco de dados
    conexao = conectar()
# Criar um cursor para executar os comandos 
    cursor = conexao.cursor()

    comando = 'INSERT INTO vendas (nome_Produto, valor) VALUES (%s, %s)' # Fazer um comando SQL
    cursor.execute(comando, (nome_Produto, valor)) # Executar o comando SQL
    conexao.commit() # edita o banco de dados

    # Fechar a conexão e o Cursor
    cursor.close()
    conexao.close()



# READ
def listar_vendas(): # ela traz tudo, sem filtro. Parâmetro é a informação que a função precisa receber de fora. Se você quisesse listar só uma venda, aí sim receberia um idVendas
# Criar uma conexão com banco de dados
    conexao = conectar()
# Criar um cursor para executar os comandos 
    cursor = conexao.cursor()


    comando = 'SELECT * FROM vendas' # Comando para ler dados
    cursor.execute(comando) # Executar o comando SQL
    resultado = cursor.fetchall() # fetchall() busca resultados e o commit confirma alterações. 

# Fechar o cursor e fechar a conexão
    cursor.close()
    conexao.close()
    return resultado

# UPDATE
def atualizar_vendas(idVendas, valor): # Eu devo colocar como parâmetros os valores cujo eu desejo atualizar
# Criar uma conexão com banco de dados
    conexao = conectar()
# Criar um cursor para executar os comandos
    cursor = conexao.cursor()

# Fazer um comando SQL
    comando = 'UPDATE vendas SET valor = %s WHERE idVendas = %s' 
# Executa o comando 
    cursor.execute(comando, (valor,idVendas))
# Edita o banco de dados
    conexao.commit()

# Fechar o cursor e a conexão
    cursor.close()
    conexao.close()  

# DELETE
def deletar_vendas(idVendas): # Dar como parâmetro o registro que você deseja apagar

    # Criar uma conexão com banco de dados
    conexao = conectar()
    # Criar um cursor para executar os comandos
    cursor = conexao.cursor()

    # Fazer um comando SQL 
    comando = 'DELETE FROM vendas WHERE idVendas = %s'
    # Executar o comando
    cursor.execute(comando, (idVendas,))
    # Editar o banco de dados 
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()



if __name__ == "__main__":
   pass
   

