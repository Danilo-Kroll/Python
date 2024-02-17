# 056 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

totalIdade = 0
maior = 0
nomeMaior = ''
homemMaior = 0
mulherMenor = 0

for p in range(1, 5):
	print("----- {}ª PESSOA -----".format(p))
	nome = str(input("Nome: "))
	idade = int(input("Idade: "))
	sexo = str(input("Sexo [M/F]: ")).upper()

	totalIdade += idade

	if idade > maior and sexo == 'M':
		maior = idade
		nomeMaior = nome
		homemMaior += 1
	if idade < 20 and sexo == 'F':
		mulherMenor += 1

print("----- RESULTADO -----")
print("A média de idade é {} anos.".format(totalIdade / 4))

if homemMaior > 0:
	print("O homem mais velho tem {} anos e se chama {}.".format(maior, nomeMaior))
else:
	print("Não possui homem nesse grupo!")

if mulherMenor > 0:
	print("São {} mulheres com menos de 20 anos.".format(mulherMenor))
else:
	print("Não possui mulheres com menos de 20 anos nesse grupo!")