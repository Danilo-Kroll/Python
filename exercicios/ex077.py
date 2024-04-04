# 077 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('programar', 'aprender', 'estudar', 'descansar', 'praticar', 'curso', 'futuro')

total = len(lista)

for l in lista:
	print(f'\nNa palavra {l.upper()} temos ', end='')
	for letra in l:
		if letra.lower() in 'aeiou': # 'aáãeéiou' => caso tenha acento
			print(letra, end=' ')