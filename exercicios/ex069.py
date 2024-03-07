# 069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

sexo = 'M'
maior = 0
homem = 0
mulherMenor = 0

while True:
	idade = int(input("Idade: "))
	sexo = ' '
	continuar = ' '

	while sexo not in 'MF':
		sexo = str(input("Sexo [M/F]: ")).upper()

	if idade > 18:
		maior += 1
	if sexo == 'M':
		homem += 1
	if sexo == 'F' and idade < 20:
		mulherMenor += 1

	while continuar not in 'SN':
		continuar = str(input("Continuar [S/N]? ")).upper()

	if continuar == 'S':
		print("")
	else:
		break

print("=" * 10)
print(f"Total de pessoas maiores de 18 anos: {maior}")
print(f"Total de homens: {homem}")
print(f"Total de mulheres com menos de 20 anos: {mulherMenor}")