# 054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year

maior = 0
menor = 0

for a in range(1, 8):
	ano = int(input("Digite o ano de nascimento: "))
	idade = atual - ano
	if idade >= 21:
		maior += 1
	else: 
		menor += 1
print("Maiores: {}".format(maior))
print("Menores: {}".format(menor))