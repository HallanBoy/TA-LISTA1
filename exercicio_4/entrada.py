from typing import Optional

def ler_inteiro(mensagem: str, mensagem_erro: str, minimo: Optional[int] = None, maximo: Optional[int] = None) -> int:
    while True:
        entrada: str = input(mensagem)
        if entrada.strip().lstrip("-").isdigit():
            valor: int = int(entrada)
            if (minimo is None or valor >= minimo) and (maximo is None or valor <= maximo):
                return valor
            else:
                print(f"Erro: o número deve estar entre {minimo} e {maximo}.")
        else:
            print(mensagem_erro)
