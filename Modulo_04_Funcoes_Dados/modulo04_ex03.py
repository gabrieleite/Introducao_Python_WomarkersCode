'''
Crie um programa que salve em um arquivo de texto
uma frase sobre o que você aprendeu no curso.'''

arquivo = "aprendizado.txt"

with open(arquivo, mode="w", encoding="utf-8") as mensagem:
    mensagem.write("Olá, eu sou a Gabi!\n")
    mensagem.write("Nesse curso tive a oportunidade de aprender o básico de Python!\n")
    mensagem.write("Aprendi conceitos básicos, laços, funções, estrutura de dados e armazenamento de arquivos\n")
    mensagem.write("Aprendi também tratamento de erros!")