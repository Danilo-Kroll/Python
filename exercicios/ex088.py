# 088 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.

from random import randint

lista = list()
dado = list()

print("="*30)
print("MEGA SENA")
print("="*30)

jogo = int(input("Quantos jogos deseja realizar: "))
qtd = 0

for c in range(0, jogo):
    for n in range(0, 6):
        num = randint(1, 61)
        if num not in dado:
            dado.append(num)

    dado.sort()            
    lista.append(dado[:])
    dado.clear()

print("="*30)

for n in range(0, jogo):
    print(f'Jogo {n+1}: {lista[n]}')