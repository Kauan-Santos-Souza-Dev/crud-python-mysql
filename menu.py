from crudpython import criar_vendas, listar_vendas, atualizar_vendas, deletar_vendas
from time import sleep
from math import isfinite

def exibir_menu():
    print("\n=== MENU DE VENDAS ===")
    print("1 - Cadastrar venda")
    print("2 - Listar vendas")
    print("3 - Atualizar valor de uma venda")
    print("4 - Deletar venda")
    print("0 - Sair")

# Funções para ler entradas do usuário com validação
def ler_opcao():
    while True: # Não é número (letra, vazio, 2.5): o int() levanta ValueError.
        entrada = input("Escolha uma opção: ").strip()
        try:
            opcao = int(entrada)
        except ValueError: # ValueError não TypeError, pois o input() sempre retorna uma string
            print("Opção inválida. Digite um número de 0 a 4.")
            continue
        # Verificar se o a opção está dentro do intervalo permitido
        if 0 <= opcao <= 4:
            return opcao
        else:
            print("Opção inválida. Digite um número de 0 a 4.")


def ler_id():
    while True:
        try:
            id_venda = int(input("ID da venda: ").strip())
            if id_venda > 0:
                return id_venda
        except ValueError:
            pass
        print("ID inválido. Digite um número inteiro maior que 0.")


def ler_nome():
    while True:
        nome = input("Nome do produto: ").strip()
        if  len(nome) > 0:
            return nome
        else:
            print("O nome não pode ficar vazio.")


def ler_valor():
    while True:
        try:
            valor = float(input("Valor: ").strip().replace(",", "."))
            if valor >= 0 and isfinite(valor):  # Verifica se o valor é maior ou igual a 0 e se é finito
                return valor
        except ValueError:
            pass
        print("Valor inválido. Digite um número maior ou igual a 0.")


# FUNÇÃO PRINCIPAL DO PROGRAMA
def main():
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 1:
            nome = ler_nome()
            valor =  ler_valor()
            criar_vendas(nome, valor)
            print("Venda cadastrada!")

        elif opcao == 2:
            vendas = listar_vendas()
            if not vendas: # Caso não haja vendas cadastradas, a lista estará vazia e o if será verdadeiro
                print("Nenhuma venda cadastrada.")
            else: # Se não estiver vazia, percorre a lista e imprime cada venda
                print("\n=== LISTA DE VENDAS ===")
                for venda in vendas:
                    print(f"ID {venda[0]} | {venda[1]} | R$ {venda[2]}")

        elif opcao == 3:
            id_venda = ler_id()
            valor =  ler_valor()
            if atualizar_vendas(id_venda,valor):
                print("Venda atualizada!")


        elif opcao == 4:
            id_venda = ler_id()
            if deletar_vendas(id_venda): # Se a função deletar_vendas retornar True, significa que a venda foi removida com sucesso
                print("Venda removida com sucesso!")
           

        elif opcao == 0:
            print("Saindo do programa...")
            sleep(1)
            print("Programa encerrado.")
            break



# a linha significa “só chame o main() se este arquivo foi executado diretamente, e não importado”
if __name__ == "__main__":
    main()
