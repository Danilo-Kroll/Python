# 052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))

c = 0

for p in range(1, n + 1):
	if n % p == 0:
		c += 1
		print("'{}'".format(p), end=" ")
	else:
		print("{}".format(p), end=" ")
print('Divisível {} vezes.'.format(c))
if c > 2:
	print('Não é PRIMO!')
else:
	print('É PRIMO!')