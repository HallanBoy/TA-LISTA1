from typing import List
from funcoes import soma, multiplica, duplicados, impares, pares, primos

def main() -> None:
    numeros: List[int] = []

    while True:
        try:
            valor: int = int(input("Digite um número inteiro (0 para sair): "))
            if valor == 0:
                break
            numeros.append(valor)
        except ValueError:
            print("Erro: por favor, digite um número inteiro válido.")

    print(f"\nLista final: {numeros}")
    print("Soma:", soma(numeros))
    print("Multiplicação:", multiplica(numeros))
    print("Duplicados:", duplicados(numeros))
    print("Ímpares distintos:", impares(numeros))
    print("Pares distintos:", pares(numeros))
    print("Primos:", primos(numeros))

if __name__ == "__main__":
    main()