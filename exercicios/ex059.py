# 059 Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

m = 0
n1 = int(input("1º valor: "))
n2 = int(input("2º valor: "))

while m != 5:
	print('''OPERAÇÃO
		[1] somar
		[2] multiplicar
		[3] maior
		[4] novos números
		[5] sair do programa''')
	m = int(input("Opção: "))
	if m == 1:
		print("{} + {}: {}".format(n1, n2, (n1 + n2)))
	elif m == 2:
		print("{} * {}: {}".format(n1, n2, (n1 * n2)))
	elif m == 3:
		if n1 > n2:
			print("{} é maior {}".format(n1, n2))
		elif n1 < n2:
			print("{} é menor {}".format(n1, n2))	
		else:
			print("{} é igual {}".format(n1, n2))
	elif m == 4:
		print("Vamos começar novamente!")
		n1 = int(input("1º valor: "))
		n2 = int(input("2º valor: "))
	elif m == 5:
		m = 5
	else:
		print("Opção inválida! Tente novamente.")
print("Até mais!!!")