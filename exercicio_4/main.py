from entrada import ler_inteiro

def main() -> None:
    numero: int = ler_inteiro(
        mensagem="Digite um número entre 10 e 100: ",
        mensagem_erro="Valor inválido. Digite um número inteiro.",
        minimo=10,
        maximo=100
    )
    print(f"Você digitou: {numero}")

if __name__ == "__main__":
    main()