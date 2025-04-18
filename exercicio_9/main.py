from funcoes import capitalizar_com_excecoes

def main() -> None:
    entrada: str = input("Digite uma frase: ")
    saida: str = capitalizar_com_excecoes(entrada)
    print(f"Resultado: {saida}")

if __name__ == "__main__":
    main()
