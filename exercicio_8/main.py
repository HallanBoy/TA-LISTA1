from typing import Any
from funcoes import capitalizar_texto

def main() -> None:
    entrada: str = input("Digite uma frase: ")
    resultado: str = capitalizar_texto(entrada)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()