# 098 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

from time import sleep

def ate10():
    print("-="*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(0, 10):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()

def ate0():
    print("-="*30)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, 0, -2):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()

def ateEscolhe():
    print("-="*30)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passos: "))

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * -1
    if inicio > fim:
        passo = passo *-1
        fim = fim-1
     
    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)


ate10()
ate0()
ateEscolhe()

# Opção 2
def contador(i, f, p):
    if i > f:
        p = p*-1
        f = f-1
    if p == 0:
        p = 1
    if p < 0:
        p *-1
    for cont in range(i, f, p):
        print(cont, end=' ', flush=True)
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passos: "))
contador(inicio, fim, passo)

# Opção 3
def contador(i, f, p):
    if p < 0:
        p *=-1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('-='*20)

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passos: "))
contador(inicio, fim, passo)