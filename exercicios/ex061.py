# 061 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

p = int(input("Primeiro termo: "))
r = int(input("Razão aritimética: "))
f = p + (10 - 1) * r

while p <= f:
	print(p, end=' ')
	p = p + r

print('')

# Opção 2
p = int(input("Primeiro termo: "))
r = int(input("Razão aritimética: "))
c = 1

while c <= 10:
	print(p, end=' ')
	c += 1
	p = p + r