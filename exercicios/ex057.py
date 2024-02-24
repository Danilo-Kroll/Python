# 057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.

s = str(input("Sexo [M/F]: ")).upper()

while s != 'S':
	s = str(input("Sexo [M/F]: ")).upper()
	if s == 'M':
		print("Masculino")
	elif s == 'F':
		print("Feminino")
	elif s != 'S':
		print("Erro! Digite novamente.")
print("SAIR")

# Opção 2
while s not in 'MmFf':
	s = str(input("Digite novamente. Sexo [M/F]: ")).upper()
if s == 'M':
	print("Masculino")
elif s == 'F':
	print("Feminino")
print("Registrado com sucesso!")