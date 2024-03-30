# 073 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol (2023), na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da São Paulo.

times = ('Palmeiras', 'Grêmio', 'Atlético Mineiro', 'Flamengo', 'Botafogo', 'Bragantino', 
	'Fluminense', 'Athletico Paranaense','Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 
	'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')

print("=" * 30)
print(f"Lista de times do Brasileirão 2023: {times}")
print("=" * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print("=" * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print("=" * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print("=" * 30)
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição.')