def metade(preco=0, formatar=False):
    resp = preco / 2
    return resp if formatar is False else formato(resp)
    # return resp if not formatar else formato(resp)


def dobro(preco=0, formatar=False):
    resp = preco * 2
    return resp if not formatar else formato(resp)


def aumentar(preco=0, taxa=0, formatar=False):
    resp = preco + (preco * taxa/100)
    return resp if not formatar else formato(resp)


def diminuir(preco=0, taxa=0, formatar=False):
    resp = preco - (preco * taxa/100)
    return resp if not formatar else formato(resp)


def formato(preco=0, formato='R$ '):
    return f'{formato}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaAum=10, taxaDim=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{formato(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaAum}% de aumento: \t{aumentar(preco, taxaAum, True)}')
    print(f'Com {taxaDim}% de redução: \t{diminuir(preco, taxaDim, True)}')
    print('-'*40)