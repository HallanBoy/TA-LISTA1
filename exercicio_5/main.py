from funcoes import ano_bissexto

ano: int = int(input("Digite um ano: "))

if ano_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")