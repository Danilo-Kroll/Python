# 032 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano: "))

resto1 = ano % 4
resto2 = ano % 100
resto3 = ano % 400

if resto1 == 0 and resto2 != 0 or resto3 == 0:
	print("É um ano bissexto".format(ano))
else:
	print("NÃO é um ano bissexto".format(ano))