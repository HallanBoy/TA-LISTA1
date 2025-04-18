def ano_bissexto(ano: int) -> bool:
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)