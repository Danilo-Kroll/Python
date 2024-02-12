# 048 Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

s = 0

for n in range(1, 501):
	if n % 3 == 0 and n % 2 != 0:
		print(n)
		s += n
print("Total: {:.2f}".format(s))

# Opção 2
s = 0
c = 0

for n in range(1, 501, 2):
	if n % 3 == 0:
		s += n
		c += 1
print("Contador: {} Total: {:.2f}".format(c, s))