'''
Crie uma função que receba o nome de uma participante e exiba uma mensagem de
boas-vindas personalizada'''

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem vinda ao curso!")

nome = input("Qual o seu nome? ")
saudacao(nome)