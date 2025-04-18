from typing import List

def capitalizar_texto(texto: str) -> str:
    palavras: List[str] = texto.split()
    capitalizadas: List[str] = [palavra.capitalize() for palavra in palavras]
    return " ".join(capitalizadas)