# 060 Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um número para caclular seu FATORIAL: "))

fatorial = 1

print("Fatorial de {}! = ".format(num), end='')

while num > 0:
	print(num, end='')
	print(' x ' if num > 1 else ' = ', end='')
	fatorial *= num
	num -= 1
print("{}".format(fatorial))

# Opção 2 - pacote
from math import factorial

n = int(input("Digite um número para caclular seu FATORIAL: "))
f = factorial(n)

print("O fatorial de {} é {}.".format(n, f))

# Opção 3 - for
num = int(input("Digite um número para caclular seu FATORIAL: "))

fatorial = 1

for c in range(num, 0, -1):
	print(c, end='')
	print(' x ' if c > 1 else ' = ', end='')
	fatorial *= c
print("{}".format(fatorial))