# 066 Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre elas (desconsiderando o flag).

soma = 0
c = 0

while True:
	n = int(input("Digite um número [999 para parar]: "))
	if n != 999:
		soma = soma + n
		c += 1
	else:
		break
print(f"Total de números digitados: {c}. Somatória: {soma}")

# Opção 2
	'''
	if n == 999:
		break
	soma = soma + n
	c += 1
	'''	