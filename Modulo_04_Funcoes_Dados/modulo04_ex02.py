'''Crie uma função que receba o número de horas de
estudo por semana e exiba uma mensagem de incentivo'''

def horas_estudo(horas):
    print(f"Você está estudando {horas} horas por dia! Parabéns, continue assim!")

horas = float(input("Horas de estudo: "))

horas_estudo(horas)