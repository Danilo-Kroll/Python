# 099 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    n_maior = cont = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
        if n > n_maior:
            n_maior = n
        
        cont +=1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior informado foi {n_maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()