# Listas em Python

cursos = ["Python", "Git", "Design", "CV"]

# Imprimindo a lista e o índice 1
print(cursos)
print(cursos[1])

# Alterando o índice 1
cursos[1] = "Git e GitHub"
print(cursos)

# Adicionando um valor 
cursos.append("Dados")
print(cursos)

# Removendo dois cursos
cursos.remove("Design") # Remove pelo valor
cursos.pop(0) # Remove pelo índice
print(cursos)