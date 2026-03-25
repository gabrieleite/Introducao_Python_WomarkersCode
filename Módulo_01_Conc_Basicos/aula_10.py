# Operações Especiais

# Exemplos de operadores 
# += Incremento
# -= Decremento
# % Resto da Divisão

valorA = int(input("Qual é o valor A? "))
valorB = int(input("Qual é o valor B? "))

valorA += 5
valorB -= 2

print("Valor final de A: ", valorA)
print("Valor final de B: ", valorB)

if valorA % 2 == 0:
    print("Valor A é par!")
else:
    print("Valor A é ímpar!")

if valorB % 2 == 0:
    print("Valor B é par!")
else:
    print("Valor B é ímpar!")