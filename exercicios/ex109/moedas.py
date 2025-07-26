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