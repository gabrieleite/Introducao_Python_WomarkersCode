# Funções 
def saudacao(nome, estado):
    print(f"{nome}, seja bem vinda! Muito bom ver alguém de {estado} no nosso curso")


# saudacao("Gabi", "São Paulo")

def soma(a, b):
    return a + b

# resultado = soma(5, 6)
# print(resultado)

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
print(verificar_idade(13))