# 026 Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra A aparece: {} vezes".format((frase.count('A'))))

print("Posição do primeiro A: {}.".format((frase.find('A')+1)))

print("Posição do primeiro A: {}.".format((frase.rfind('A')+1)))