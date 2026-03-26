# Desafio de Lógica: Dominando Repetições com While

''' Objetivo
O desafio é criar uma menu interativo. O diferencial
aqui é que o programa não vai apenas rodar e fechar;
ele deve continuar "vivo" e disponível para a usuária
até que ela decida encerrar a navegação.'''

contador = 0 
opcao = 0
print("MENU INTERATIVO")
nome = input("Qual o seu nome? ")
while opcao != 3:
    contador += 1
    print("--------------------------------------------------")
    print("Olá,", nome)
    print("Seja bem-vinda ao nosso menu")
    print("1 - Verificar maioridade")
    print("2 - Fazer uma soma")
    print("3 - Sair do menu")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print("Menu 1 - Verificar maioridade")
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Você é maior de idade!")
        else:
            print("Você é menor de idade")
    elif opcao == 2:
        print("Menu 2 - Fazer uma soma")
        valorA = float(input("Digite o valor A: "))
        valorB = float(input("Digite o valor B: "))
        soma = valorA + valorB
        print("O resultado da sua soma é:", soma)  
    elif opcao > 3 or opcao < 1:
        print("--------------------------------------------------")
        print("Por favor, digite um número válido!") 

print("---------------------------------------")
print("Muito obrigada, volte sempre que quiser! :)")
print("O menu foi exibido", contador, "vez(es)!") 
    

    