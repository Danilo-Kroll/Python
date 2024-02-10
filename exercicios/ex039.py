# 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano = int(input("Informe seu ano de nascimento: "))

idade = datetime.date.today().year - ano

alistar = idade - 18

if idade < 18:
	print("Ainda não está no prazo de se alistar! {} anos.".format(idade))
	print("Faltam {} anos para os seu alistamento.".format(alistar * -1))
elif idade == 18:
	print("É hora de se alistar! {} anos.".format(idade))
else:
	print("Passou do tempo do alistamento! {} anos.".format(idade))
	print("Já se passaram {} anos do seu alistamento.".format(alistar))