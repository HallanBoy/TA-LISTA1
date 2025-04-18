from typing import List

def adicionar_cliente(fila: List[str], nome: str) -> None:
    fila.append(nome)

def atender_cliente(fila: List[str]) -> str:
    if not fila:
        raise IndexError("Fila vazia. Nenhum cliente para atender.")
    return fila.pop(0)