# Construindo meu primeiro sistema de cadastro

# Objetivo
# O objetivo deste exercício é consolidar os fundamentos
# de Python, transformando conceitos técnicos em um 
# programa funcional que interage com o usuário, processa
# informações e toma decisões lógicas.

# Coleta das Informações (Nome, Idade, Altura, Ano atual)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))
ano_atual = int(input("Ano atual: "))

# Mensagem de boas-vindas
print("\nOlá,", nome,"\nSeja bem-vinda ao mundo do Python!")


# Processamento e Cálculos
ano_nasc = ano_atual - idade
dobro = idade * 2
idade_elevada = idade ** 2
idade += 5

print("\nProcessamento e Cálculos")
print("Você nasceu em", ano_nasc)
print("Daqui a 5 anos você terá", idade)
print("O dobro da sua idade:", dobro)
print("Sua idade elevada ao quadrado:", idade_elevada)

# Lógica e Comparação
print("\nLógica e Comparação")

idade -= 5

if idade >= 18:
    print("Você é maior de idade!")
else: 
    print("Você é menor de idade")

print("A altura mínima é maior ou igual a 1.60m?")

if altura >= 1.60:
    print("Sim!")
else: 
    print("Não!")

print("\nObrigada por participar!!")

