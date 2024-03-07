# 070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

soma = 0
maiorMil = 0
produtoBarato = ''
precoBarato = 0
c = 0

while True:
	produto = str(input("Nome do produto: ")).upper()
	preco = float(input("Preço do produto: R$"))
	soma = soma + preco
	c += 1

	continuar = ' '

	while continuar not in 'SN':
		continuar = str(input("Continuar? [S/N]")).upper()
	
	if preco > 1000:
		maiorMil += 1

	if c == 1:
		precoBarato = preco
		produtoBarato = produto
	else:
		if preco < precoBarato:
			precoBarato = preco
			produtoBarato = produto

	if continuar == 'N':
		break

print(f"Total da itens: {c}")
print(f"Total da compra: R${soma:.2f}")
print(f"Quantidade de produtos acima de R$1000.00: {maiorMil}")
print(f"Produto mais barato: {produtoBarato} = R${precoBarato:.2f}")