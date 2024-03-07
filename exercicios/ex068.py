# 068 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

ganho = 0

while True:
	numJogador = int(input("Digite um valor: "))
	tipo = ' '

	while tipo not in 'PI':
		tipo = str(input("Par ou Ímpar?: [P/I]")).upper()

	numComputador = randint(0, 10)
	soma = numJogador + numComputador
	resultado =  soma % 2

	if resultado == 0:
		tipoFinal = 'P'
		tipoNome = 'PAR'
	else:
		tipoFinal = 'I'
		tipoNome = 'ÍMPAR'

	if tipoFinal == tipo:
		print(f"Você jogou {numJogador} x e o computador {numComputador} = Total {soma} é {tipoNome}")
		print("Você GANHOU!")
		print("Jogue novamente!")
		ganho += 1
	else:
		print(f"Você jogou {numJogador} e o computador {numComputador} = Total {soma} é {tipoNome}")
		print("Você PERDEU!")
		break

print(f"GAME OVER! Você venceu {ganho} vezes.")