# 093 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

jogador['Jogador'] = str(input('Nome do Jogador: '))
totalJogos = int(input(f'Total de Jogos do {jogador["Jogador"]}: '))

for c in range(0, totalJogos):
    golsFeitos = gols.append(int(input(f'   Total de gols na {c+1}ª partida: ')))

jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print("-="*30)
print(jogador)

print("-="*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
    
print("-="*30)
print(f'O jogador {jogador["Jogador"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')