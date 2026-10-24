# Instalar o mysql-connector-python "pip install mysql-connector-python"
# Esconder Senhas: pip install python-dotenv
# É um módulo que já vem com o Python e serve para conversar com o sistema operacional. Aqui você só usa uma coisa dele: os.getenv("NOME"), que lê uma variável de ambiente, 
# um valor guardado na memória do processo, fora do seu código. Se a variável não existir, devolve None.
import os
import mysql.connector
from mysql.connector import Error # from mysql.connector import Error é um atalho, não uma necessidade. O Error já está acessível só com import mysql.connector, pelo caminho completo:
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
def criar_vendas(nome_Produto, valor):
    conexao = None   # gavetas vazias (evita erro no finally)
    cursor = None

    try:
        conexao = conectar()                 # abre a conexão com a função conectar(), que conecta ao banco de dados
        cursor = conexao.cursor()            # cria o cursor, que executa os comandos SQL

        comando = 'INSERT INTO vendas (nome_Produto, valor) VALUES (%s, %s)'
        cursor.execute(comando, (nome_Produto, valor))   # executa o INSERT
        conexao.commit()                     # salva de verdade

        if cursor.rowcount == 0:
            print("Nenhuma venda cadastrada.")
        elif cursor.rowcount >= 1:
            print(f"{cursor.rowcount} venda(s) cadastrada(s).")
        else:
            print(" Erro ao cadastrar venda.") 

    except Error as e:
        if conexao:                          # só desfaz se a conexão existe
            conexao.rollback()               # descarta o que não foi salvo
        print(f"Erro ao cadastrar venda: {e}")

    finally:
        if cursor:
            cursor.close()                 # fecha o cursor
        if conexao:
            conexao.close()                # fecha a conexão com o banco de dados


# READ
def listar_vendas(): # ela traz tudo, sem filtro. Parâmetro é a informação que a função precisa receber de fora. Se você quisesse listar só uma venda, aí sim receberia um idVendas

    conexao = None
    cursor = None
    resultado = []                       # devolvido se der erro (lista vazia)

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        comando = 'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()    # guarda todas as linhas

    except Error as e:
        print(f"Erro ao listar vendas: {e}")

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

    return resultado                     # fora do try: sempre devolve algo

# UPDATE
def atualizar_vendas(idVendas, valor): # Eu devo colocar como parâmetros os valores cujo eu desejo atualizar
    conexao = None
    cursor =  None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        comando = 'UPDATE vendas SET valor = %s WHERE idVendas = %s'
        cursor.execute(comando, (valor, idVendas))
        conexao.commit()

        if cursor.rowcount == 0:
            print(f'Nenhuma venda alterada, ID {idVendas} não existe ou valor já era esse:')
        else:
            print(f'{valor} inserido com sucesso em ID {idVendas}')

    except Error as e:
        if conexao:
            conexao.rollback() 
        print(f'Erro ao atualizar venda {e}')

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        


# DELETE
def deletar_vendas(idVendas): # Dar como parâmetro o registro que você deseja apagar
    conexao = None   # gavetas vazias (evita erro no finally)
    cursor = None

    try:
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

        if cursor.rowcount == 0: # Cursor que executa os comandos portanto ele deve receber o rowcount.
            print("Nenhuma venda com ID {idVendas} encontrada.")
        else:
            print(f"{cursor.rowcount} venda(s) selecionada(s).")

    except Error as e:
        if conexao:                          # só desfaz se a conexão existe
            conexao.rollback()               # descarta o que não foi salvo
        print(f"Erro ao deletar venda: {e}")

    # Fechar o cursor e a conexão
    finally:
        if cursor:
            cursor.close()                 # fecha o cursor
        if conexao:
            conexao.close()                # fecha a conexão com o banco de dados



if __name__ == "__main__":
   pass
   

