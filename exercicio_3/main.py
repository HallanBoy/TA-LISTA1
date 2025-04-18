from entrada import ler_inteiro

def main() -> None:
    numero: int = ler_inteiro(
        mensagem="Digite um número inteiro: ",
        mensagem_erro="Erro: valor inválido. Por favor, digite um número inteiro."
    )
    print(f"Você digitou: {numero}")

if __name__ == "__main__":
    main()