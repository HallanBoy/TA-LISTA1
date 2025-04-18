from typing import List
from funcoes import soma, multiplica, duplicados, impares, pares, primos

def main() -> None:
    print("Digite os números separados por espaço (0 encerra a entrada):")
    entrada: str = input(">> ").strip()

    numeros: List[int] = list(map(int, entrada.split()))
    numeros = numeros[:numeros.index(0)] if 0 in numeros else numeros

    print(f"\nLista final: {numeros}")
    print("Soma:", soma(numeros))
    print("Multiplicação:", multiplica(numeros))
    print("Duplicados:", duplicados(numeros))
    print("Ímpares distintos:", impares(numeros))
    print("Pares distintos:", pares(numeros))
    print("Primos:", primos(numeros))

if __name__ == "__main__":
    main()
