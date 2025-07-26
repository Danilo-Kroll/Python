# 085 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.

lista = list()
dadoPar = list()
dadoImpar = list()
dado = list()

for n in range(0, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        dadoPar.append(num)               
    else:
        dadoImpar.append(num)
        
lista.append(dadoPar[:])
lista.append(dadoImpar[:])

# Opção 2
# No lugar de dadoPar e dadoImpar usar:
'''
lista = [[], []]
if num % 2 == 0:
    lista[0].append(num) --> par
else:
    lista[1].append(num) --> impar

list[0].sort()
list[1].sort()
'''

lista.sort(reverse=True)
print(lista)
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')