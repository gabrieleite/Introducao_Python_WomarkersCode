# Manipulação de Arquivos
import os # Permite interagir com o sistema operacional


arquivo = "alunas.txt"

alunas = []


# Alterar arquivo
# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     alunas = lista.readlines()

# alunas_atualizadas = []

# for aluna in alunas:
#     nome = aluna.strip()
#     if nome != "Carla":
#         alunas_atualizadas.append(nome)

# with open(arquivo, mode="w", encoding="utf-8") as lista:
#     for aluna in alunas_atualizadas:
#         lista.write(aluna + "\n")

# # a: append
# with open(arquivo, mode="a", encoding="utf-8") as lista:
#     lista.write("Daniela\n")


if os.path.exists(arquivo): 
    os.remove(arquivo)
    print("Arquivo excluído com sucesso!")
else: 
    print("Arquivo não encontrado!")