# Condições com if, else e elif em Python

nota1 = 10
nota2 = 6
nota3 = 7.5

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Aprovada! - NOTA:", round(media, 2))
elif media >= 5:
    print("Recuperação! - NOTA:", round(media, 2))
else:
    print("Reprovada! - NOTA:", round(media, 2))