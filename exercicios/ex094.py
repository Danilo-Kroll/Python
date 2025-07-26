# 094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista = list()
pessoas = dict()
soma = cont = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Digite o nome: "))

    while True:
        pessoas['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Informação inválida!')

    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade']
    cont += 1

    lista.append(pessoas.copy())
 
    while True:
        continuar = str(input("Continuar [S/N]: ")).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Somente S ou N')
    if continuar == 'N':
        break

print(lista)

media = soma / cont

print('-=-=-=-=-=-= ANÁLISE =-=-=-=-=-=-')
print(f'1. O grupo tem {len(lista)} pessoas.')
print(f'2. A média de idade é de {media:5.2f} anos.')
print(f'3. As mulheres cadastradas foram:', end="")
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'4. Lista das pessoas que estão com idade acima da média:')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')