'''
Leia o conteúdo criado no exercício anterior e exiba
na tela
'''

arquivo = "aprendizado.txt"


with open(arquivo, mode="r", encoding="utf-8") as mensagem:
    conteudo = mensagem.read()

print(conteudo)