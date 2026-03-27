'''
Atualize a área de interesse no dicionário criado
anteriormente e exiba o novo valor.
'''

sobre_mim = {
    "nome": "Gabriela", 
    "cidade": "Ribeirão Pires", 
    "area_interesse": "Dados"
}

print(f"Nome: {sobre_mim['nome']}")
print(f"Cidade: {sobre_mim['cidade']}")
print(f"Área de Interesse: {sobre_mim['area_interesse']}")

sobre_mim['area_interesse'] = "Desenvolvimento Mobile"

print("-" * 20)
print(f"Nova área de interesse: {sobre_mim['area_interesse']}")