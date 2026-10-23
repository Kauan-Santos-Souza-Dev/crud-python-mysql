from crudpython import criar_vendas, listar_vendas, atualizar_vendas, deletar_vendas
from time import sleep

def exibir_menu():
    print("\n=== MENU DE VENDAS ===")
    print("1 - Cadastrar venda")
    print("2 - Listar vendas")
    print("3 - Atualizar valor de uma venda")
    print("4 - Deletar venda")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            valor = float(input("Valor: "))
            criar_vendas(nome, valor)
            for valor in range(6): # range(5) significa que o for vai se repetir 5 vezes
                sleep(0.8) # sleep() faz o programa esperar um tempo antes de continuar
                print(".", end="",flush=True) # flush=True força a impressão imediata do ponto
            print("Venda cadastrada!")

        elif opcao == "2":
            vendas = listar_vendas()
            for venda in vendas:
                print(f"ID {venda[0]} | {venda[1]} | R$ {venda[2]}")

        elif opcao == "3":
            id_venda = int(input("ID da venda: "))
            valor = float(input("Novo valor: "))
            atualizar_vendas(valor, id_venda)
            for valor in range(6): # range(5) significa que o for vai se repetir 5 vezes
                sleep(0.8) # sleep() faz o programa esperar um tempo antes de continuar
                print(".", end="",flush=True) # flush=True força a impressão imediata do ponto
            print("Venda atualizada!")

        elif opcao == "4":
            id_venda = int(input("ID da venda: "))
            deletar_vendas(id_venda)
            for valor in range(6): # range(5) significa que o for vai se repetir 5 vezes
                sleep(0.8) # sleep() faz o programa esperar um tempo antes de continuar
                print(".", end="",flush=True) # flush=True força a impressão imediata do ponto
            print("Venda removida!")

        elif opcao == "0":
            print("Encerrando", end="") # end=""  evita a quebra de linha
            for valor in range(6): # range(5) significa que o for vai se repetir 5 vezes
                sleep(0.8) # sleep() faz o programa esperar um tempo antes de continuar
                print(".", end="",flush=True) # flush=True força a impressão imediata do ponto
            print()
            break


# a linha significa “só chame o main() se este arquivo foi executado diretamente, e não importado”
if __name__ == "__main__":
    main()