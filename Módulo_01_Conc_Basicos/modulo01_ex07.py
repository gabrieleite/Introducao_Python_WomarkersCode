'''
Crie duas variáveis com números inteiros representando

- Número de aulas assistidas
- Número total de aulas do curso

Calcule e exbia quantas aulas ainda faltam'''

total_aulas = int(input("Qual o total de aulas do curso? "))
aulas_assistidas = int(input("Quantas aulas já assistiu? "))
resultado = total_aulas - aulas_assistidas

print("Aindam faltam", resultado, "aulas para serem assistidas!")