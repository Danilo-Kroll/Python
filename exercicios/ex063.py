# 063 Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. 

termo = int(input("Quantos termos você quer mostrar: "))
c = 3

n1 = 0
n2 = 1
f = 0

print("{} {}".format(n1, n2), end=' ')
while c <= termo:
	c += 1
	f = n1 + n2
	n1 = n2
	n2 = f
	print(f, end=' ')