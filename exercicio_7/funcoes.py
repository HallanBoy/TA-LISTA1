from typing import List

def adicionar_cliente(pilha: List[str], nome: str) -> None:
    pilha.append(nome)

def atender_cliente(pilha: List[str]) -> str:
    if not pilha:
        raise IndexError("Pilha vazia. Nenhum cliente para atender.")
    return pilha.pop()  # LIFO: remove o último cliente
