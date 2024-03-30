# 075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = (int(input('Digite o 1º número: ')),
	int(input('Digite o 2º número: ')),
	int(input('Digite o 3º número: ')), 
	int(input('Digite o 4º número: ')))

print(f'Os números digitados foram: {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
# Opção 2
# if 3 in lista:
if lista.count(3) > 0:
	print(f'O valor 3 está na {lista.index(3) + 1}ª posição')
else:
	print(f'O valor 3 não foi digitado em nehuma posição')

print('Os valores pares digitados foram: ', end='')
for n in lista:
	if n % 2 == 0:
		print(n, end=' ')