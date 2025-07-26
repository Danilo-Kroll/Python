# 100 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    print('Sorteio de 5 valores:', end=' ')
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
    print(numeros)

def somaPar(lista):
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    print(f'A soma dos números pares da lista {lista} é {par}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)