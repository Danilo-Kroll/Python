# 072 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
	'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
	'vinte')

while True:
	num = int(input('Digite um número de 0 até 20: '))
	while num < 0 or num > 20:
		num = int(input('Tente novamente. Digite um número de 0 até 20: '))
	break

print(tupla[num])