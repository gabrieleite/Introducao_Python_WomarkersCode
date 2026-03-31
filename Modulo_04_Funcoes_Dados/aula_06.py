# Tratamento de Erros

# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10 / numero
# except ZeroDivisionError: # Erro divisão por 0
#     print("Não é possível dividir por 0!")
# except ValueError: # Erro de valor
#     print("Digite somente números!")
# else:
#      print(f"Resultado: {resultado}")

try:
    arquivo = open("dados.txt", mode="r")
    conteudo = arquivo.read()
except FileNotFoundError: # Arquivo não encontrado
    print("Arquivo não encontrado")
finally: # Sempre é executado, com ou sem erro!
    print("Operação finalizada!")