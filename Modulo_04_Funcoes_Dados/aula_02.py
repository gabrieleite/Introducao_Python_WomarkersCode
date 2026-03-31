# Manipulação de Arquivos

arquivo = "alunas.txt"

with open(arquivo, mode="w", encoding="utf-8") as lista:
    lista.write("Ana\n")
    lista.write("Beatriz\n")
    lista.write("Carla\n")