# 030 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número: "))

resultado = num % 2

if resultado > 0:
	print("O número {} é ÍMPAR".format(num))
else:
	print("O número {} é PAR".format(num))