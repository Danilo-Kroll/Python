# 092 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

from datetime import datetime

pessoa = dict()

pessoa['Nome'] = str(input('Digite o nome: '))
ano = int(input('Ano de Nascimento: '))
idade = datetime.now().year - ano
pessoa['Idade'] = idade
pessoa['Carteira'] = int(input('Nº Carteira (0 não possui): '))

if pessoa['Carteira'] != 0:
    pessoa['Ano Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Qual o Salário: R$ '))
    anoAponsenta = (pessoa['Ano Contratação'] + 35) - ano
    pessoa['Aposentar'] = anoAponsenta

print("-="*30)
print(pessoa)

for k, v in pessoa.items():
    print(f'{k}: {v}')