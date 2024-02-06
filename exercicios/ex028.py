# 028 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o 
# usuário tentar descobrir qual foi o número escolhido pelo computador. O Programa deverá escrever na tela
# se o usuário venceu ou perdeu.

from random import randint

escolha = randint(0, 5)

num = int(input("Escolha um número: "))

if num == escolha:
	print("VOCÊ ACERTO!! O número escolhido foi {}, e você escolheu {}.".format(escolha, num))
else:
	print("VOCÊ ERROU!! O número escolhido foi {}, e você escolheu {}.".format(escolha, num))