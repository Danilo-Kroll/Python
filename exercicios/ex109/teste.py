# 109 Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida
# no desafio 108.

import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.formato(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.formato(p)} é {moedas.dobro(p, False)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Aumentando 13%, temos {moedas.diminuir(p, 13, True)}')