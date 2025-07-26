# 084 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = list()
dado = list()
listaMaior = []
listaMenor = []
maior = menor = 0
cont = 1

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    dado.append(nome)
    dado.append(peso)
    lista.append(dado[:])
    dado.clear()

    if cont == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso            
        elif peso < menor:
            menor = peso
    cont += 1

    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar in 'Nn':
        break
    
for p in lista:
    if p[1] == maior:
        listaMaior.append(p[0])
    if p[1] == menor:
        listaMenor.append(p[0])

# Opção 2
# FOR na 'lista' SE o maior e menor é o nome, sem precisar criar listaMaior e listaMenor
'''
for p in lista:
    in p[1] == maior:
        print(f'[{p[0]} ', end='')
print()
for p in lista:
    in p[1] == menor:
        print(f'[{p[0]} ', end='')
print()
'''

print(lista)
print(f'Foram cadasradas {len(lista)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de {listaMaior}')
print(f'O maior peso foi {menor}Kg. Peso de {listaMenor}')