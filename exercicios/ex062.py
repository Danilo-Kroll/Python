# 062 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

p = int(input("Primeiro termo: "))
r = int(input("Razão aritimética: "))
c = 1

total = 0
mais = 10

while mais != 0:
	total = total + mais
	while c <= total:
		print(p, end=' ')
		c += 1
		p = p + r
	print('PAUSA')
	mais = int(input("Quantos termos a mais deseja mostrar: "))
print("Finalizado com {} termos.".format(total))