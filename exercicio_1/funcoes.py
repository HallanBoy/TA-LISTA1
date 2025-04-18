from typing import List

def soma(lista: List[int]) -> int:
    return sum(lista)

def multiplica(lista: List[int]) -> int:
    resultado: int = 1
    for num in lista:
        resultado *= num
    return resultado

def duplicados(lista: List[int]) -> List[int]:
    return list({x for x in lista if lista.count(x) > 1})

def impares(lista: List[int]) -> List[int]:
    return list({x for x in lista if x % 2 != 0})

def pares(lista: List[int]) -> List[int]:
    return list({x for x in lista if x % 2 == 0})

def primos(lista: List[int]) -> List[int]:
    def e_primo(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list({x for x in lista if e_primo(x)})
