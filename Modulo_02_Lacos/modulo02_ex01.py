'''
Crie uma variável com a quantidade de aulas concluídas.
Se for maior ou igual a 5, exiba "Bom progresso!". Caso
contrário, exiba "Continue estudando".'''

qtd_aulas_assistidas = int(input("Quantas aulas você já assistiu? "))

if qtd_aulas_assistidas >= 5:
    print("Bom progresso!")
else:
    print("Continue estudando")