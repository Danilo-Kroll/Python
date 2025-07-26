# 108 Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.

# import ex108.moedas
import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.formato(p)} é {moedas.formato(moedas.metade(p))}')
print(f'O dobro de {moedas.formato(p)} é {moedas.formato(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.formato(moedas.aumentar(p, 10))}')
print(f'Aumentando 13%, temos {moedas.formato(moedas.diminuir(p, 13))}')