# Dicionários e listas de Dados em Python

# print(aluna["nome"])

# aluna["idade"] = 54
# aluna["cidade"] = "São Paulo"

# print(aluna)

# aluna.pop("idade")
# print(aluna)

escola = [
    {
        "nome": "Ana",
        "idade": 22,
        "curso": "Python", 
        "status": True
    },
    {
        "nome": "Gabriela",
        "idade": 23,
        "curso": "C#", 
        "status": True
    },
    {
        "nome": "Rayssa",
        "idade": 24,
        "curso": "Angular", 
        "status": True
    },
    {
        "nome": "Dennis",
        "idade": 21,
        "curso": "SRE", 
        "status": False
    }
]


# aluna = escola[2]

# print(aluna)

# print(escola)

# for aluna in escola:
#     print(f"Nome: {aluna['nome']}")
#     print(f"Curso: {aluna['curso']}")
#     print("-" * 20)

for aluna in escola:
    if aluna["nome"] == "Ana":
        print(f"Nome: {aluna['nome']}")
        print(f"Curso: {aluna['curso']}")

# nome_da_escola = "WoMakers"

# print(f"Escola: {nome_da_escola}")