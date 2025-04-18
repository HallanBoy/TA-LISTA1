from typing import List
from funcoes import adicionar_cliente, atender_cliente

def main() -> None:
    pilha: List[str] = []

    while True:
        print("\n--- Menu Pilha de Banco ---")
        print("1 - Adicionar cliente")
        print("2 - Atender cliente")
        print("3 - Fim")
        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            nome: str = input("Nome do cliente: ").strip()
            adicionar_cliente(pilha, nome)
            print(f"Cliente '{nome}' adicionado à pilha.")
        elif opcao == "2":
            try:
                cliente_atendido: str = atender_cliente(pilha)
                print(f"Cliente '{cliente_atendido}' foi atendido.")
            except IndexError:
                print("Não há clientes na pilha.")
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
