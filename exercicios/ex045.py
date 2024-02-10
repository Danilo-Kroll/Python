# 045 Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("""[0] Pedra
[1] Papel
[2] Tesoura""")

jokJ = int(input("Opção: "))
jokC = randint(0, 2)

if jokJ == 0 and jokC == 1:
	print("{} x {}. Você perdeu!".format(jokJ, jokC))
elif jokJ == 0 and jokC == 2:
	print("{} x {}. Você ganhou!".format(jokJ, jokC))
elif jokJ == 1 and jokC == 0:
	print("{} x {}. Você ganhou!".format(jokJ, jokC))
elif jokJ == 1 and jokC == 2:
	print("{} x {}. Você perdeu!".format(jokJ, jokC))
elif jokJ == 2 and jokC == 0:
	print("{} x {}. Você perdeu!".format(jokJ, jokC))
elif jokJ == 2 and jokC == 1:
	print("{} x {}. Você perdeu!".format(jokJ, jokC))
elif jokJ == jokC:
	print("{} x {}. Empatou!".format(jokJ, jokC))
else:
	print("{}. Opção inválida!".format(jokJ))

# Opção 2
itens = ('Pedra', 'Papel', 'Tesoura')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print("-=" * 10)
print("Computador {}".format(itens[jokC]))
print("Jogador {}".format(itens[jokJ]))
print("-=" * 10)

if jokC == 0:
	if jokJ == 0:
		print("Empate!")
	elif jokJ == 1:
		print("Jogador vence!")
	elif jokJ == 2:
		print("Computador vence!")
	else:
		print("Inválida!")
elif jokC == 1:
	if jokJ == 0:
		print("Computador vence!")
	elif jokJ == 1:
		print("Empate!")
	elif jokJ == 2:
		print("Jogador vence!")
	else:
		print("Inválida!")
elif jokC == 2:
	if jokJ == 0:
		print("Jogador vence!")
	elif jokJ == 1:
		print("Computador vence!")
	elif jokJ == 2:
		print("Empate!")
	else:
		print("Inválida!")