# 064 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
c = 0
soma = 0

while n != 999:
	n = int(input("Digite um número [999 para parar]: "))
	if n != 999:
		c += 1
		soma = soma + n
		print(soma)
print("Total de números digitados: {}. Somatória: {}".format(c, soma))