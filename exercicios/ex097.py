# 097 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.

def linha(texto):
    print('-' * len(texto)*2)
    print(texto)
    print('-' * len(texto)*2)
    

linha(str(input('Digite um texto: ')))