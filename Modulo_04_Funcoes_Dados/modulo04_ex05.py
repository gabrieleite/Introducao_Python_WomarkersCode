'''
Crie um programa que peça ao usuário um número. Use
try e except para evitar erri caso seja digitado um valor
inválido!
'''

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite somente números!")
else:
    print(f"O número digitado foi: {numero}")
finally:
    print("Operação finalizada!")