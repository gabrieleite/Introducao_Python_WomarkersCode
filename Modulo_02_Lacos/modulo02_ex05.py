'''
Crie uma variável com a idade de uma pessoa. Use IF
e ELSE para verificar se ela pode se inscrever em um
curso que exige idade mínima de 16 anos.'''

idade = int(input("Qual a sua idade? "))

if idade >= 16: 
    print("Você está APTA para se inscrever no curso!")
else:
    print("Você NÃO está apta para se inscrever no curso!")