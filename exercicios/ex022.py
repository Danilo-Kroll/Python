# 022 Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()

# Maiúscula e Minúscula
print(nome.upper())
print(nome.lower())

# Quantidade de letras (com espaço)
print(len(nome))

# Quantidade de letras (sem espaço)
print(len(nome) - nome.count(' '))

# Quantidade de letras do primeiro nome
## Opção 1
print(nome.find(' '))

## Opção 2
dividido = nome.split()
print(len(dividido[0]))