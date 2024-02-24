# 065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'

c = soma = media = maior = menor = 0

while continuar != 'N':
	n = int(input("Digite um número: "))
	soma = soma + n
	c += 1
	media = soma / c
	if c == 1:
		maior = n
		menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n
	continuar = str(input("Continuar [S/N]? ")).upper()
print("Média: {:.1f}, Maior: {}, Menor: {}".format(media, maior, menor))