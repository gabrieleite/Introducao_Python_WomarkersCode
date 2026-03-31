# Manipulação de Arquivos

arquivo = "alunas.txt"

alunas = []

# Código comentado pois o arquivo já existe
# w: write
# with open(arquivo, mode="w", encoding="utf-8") as lista:
#     lista.write("Ana\n")
#     lista.write("Beatriz\n")
#     lista.write("Carla\n")

# r: read
# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     conteudo = lista.read()

# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     contador = 0
#     for linha in lista:
#         contador += 1
#         print(f"Aluna {contador}:", linha.strip())

# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     linhas = lista.readlines()

# Alterar arquivo
with open(arquivo, mode="r", encoding="utf-8") as lista:
    alunas = lista.readlines()

alunas_atualizadas = []

for aluna in alunas:
    nome = aluna.strip()
    if nome != "Carla":
        alunas_atualizadas.append(nome)

with open(arquivo, mode="w", encoding="utf-8") as lista:
    for aluna in alunas_atualizadas:
        lista.write(aluna + "\n")

# a: append
with open(arquivo, mode="a", encoding="utf-8") as lista:
    lista.write("Daniela\n")