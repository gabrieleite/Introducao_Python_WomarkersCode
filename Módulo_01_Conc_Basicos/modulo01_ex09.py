'''
Use o operador % para verificar se o número de horas
totais de estudo na semana é par ou ímpar
'''

horas_semanais = int(input("Quantas horas você estuda por semana? "))

if horas_semanais % 2 == 0:
    print("Par")
else:
    print("Ímpar")