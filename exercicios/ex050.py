# 050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0

for n in range(1, 7):
	num = int(input("Digite um número: "))
	if num % 2 == 0:
		s += num
print("Total: {}".format(s))