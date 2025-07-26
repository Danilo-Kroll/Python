# 087 Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = list()
dado = list()
cont = 0
pares = 0
tercColuna = 0
maior = 0

while cont <= 2:
    for c in range (0, 3):
        num = int(input(f"Digite um valor para [{cont}, {c}]: "))
        dado.append(num)

        # Somar valores pares
        if num % 2 == 0:
            pares += num
        
        # Somar terceira coluna
        if c == 2:
            tercColuna += num

        # Maior valor segunda linha
        if cont == 1 and c == 0:
            maior = num
        elif cont == 1 and c > 0:
            if num > maior:
                maior = num

    cont += 1
    lista.append(dado[:])
    dado.clear()

print(lista)
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')

print(f'soma valores pares {pares}')
print(f'soma da terceira coluna {tercColuna}')
print(f'maior valor da segunda linha {maior}')

# Opção 2
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print("-="* 30)
print(f'A soma dos valores pares é {spar}')
for l in range (0, 3):
    scol += matriz[1][c]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
'''