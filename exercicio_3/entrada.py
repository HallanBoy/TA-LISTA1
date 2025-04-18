def ler_inteiro(mensagem: str, mensagem_erro: str) -> int:
    while True:
        entrada: str = input(mensagem)
        if entrada.strip().lstrip("-").isdigit():
            return int(entrada)
        else:
            print(mensagem_erro)
