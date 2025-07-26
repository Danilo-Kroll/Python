# 101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO') # -> return f'{idade} anos: VOTO NEGADO.' -> print no sistema principal
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


ano = int(input('Em que ano você nasceu? '))
voto(ano)

# print(voto(ano))