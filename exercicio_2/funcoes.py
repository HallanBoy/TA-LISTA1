from typing import List
from functools import reduce

def soma(lista: List[int]) -> int:
    return sum(lista)

def multiplica(lista: List[int]) -> int:
    return reduce(lambda x, y: x * y, lista, 1)

def duplicados(lista: List[int]) -> List[int]:
    return list({x for x in lista if lista.count(x) > 1})

def impares(lista: List[int]) -> List[int]:
    return list({x for x in lista if x % 2 != 0})

def pares(lista: List[int]) -> List[int]:
    return list({x for x in lista if x % 2 == 0})

def primos(lista: List[int]) -> List[int]:
    def e_primo(n: int) -> bool:
        return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))
    
    return list({x for x in lista if e_primo(x)})
