# 095 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

lista = list()
jogador = dict()
gols = list()

print('-'*30)
while True:
    jogador.clear()
    jogador['Jogador'] = str(input('Nome do Jogador: '))
    totalJogos = int(input(f'Total de Jogos do {jogador["Jogador"]}: '))
    gols.clear()
    for c in range(0, totalJogos):
        golsFeitos = gols.append(int(input(f'   Total de gols na {c+1}ª partida: ')))

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

    lista.append(jogador.copy())

    while True:
        continuar = str(input("Continuar [S/N]: ")).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Somente S ou N')
    if continuar == 'N':
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-="*30)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do jogador {lista[busca]["Jogador"]}:')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f'    No logo {i+1} fez {g} gols.')
    print('-'*40)
print('Volte Sempre!')