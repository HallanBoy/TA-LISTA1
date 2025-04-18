from typing import List

def capitalizar_com_excecoes(texto: str) -> str:
    excecoes: List[str] = [
        "a", "o", "as", "os",
        "de", "do", "da", "dos", "das",
        "em", "no", "na", "nos", "nas",
        "por", "para", "com", "sem", "à", "ao"
    ]
    palavras: List[str] = texto.split()
    resultado: List[str] = [
        palavra.capitalize() if palavra.lower() not in excecoes else palavra.lower()
        for palavra in palavras
    ]
    return " ".join(resultado)