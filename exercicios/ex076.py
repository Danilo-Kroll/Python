# 076 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Arroz', 10, 'Feijão', 6.99, 'Frango', 5.97, 'Batata', 9.50, 'Cenoura', 4.67)

total = len(listagem)

print('=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('=' * 30)

c = 0

while c < total:
	letra = 20 - len(listagem[c])
	print(f'{listagem[c]}', end='.' * letra)
	print(f'R$ {listagem[c + 1]:>7.2f}')

	c += 2

print('=' * 30)

# Opção 2

for pos in range(0, len(listagem)):
	if pos % 2 ==0:
		print(f'{listagem[pos]:.<20}', end='')
	else:
		print(f'R${listagem[pos]:>7.2f}')