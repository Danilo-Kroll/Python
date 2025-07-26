# 078 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi 
# o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0
posicao = 0

for n in range(0, 5):
    num = int(input(f"Digite um número para a posição {n}: "))
    lista.append(num)

    if n == 0:
        maior = menor = num
        posicao = 0
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        
        posicao += 1

print(lista)
print(f"O MAIOR número digitado foi {maior}, suas posições são ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end='')
print()
print(f"O MENOR número digitado foi {menor}, suas posições são ", end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end='')