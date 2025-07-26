# 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas():
    """
    -> Cálculo estatístico de notas.
    :param n: Os númros a serem calculados.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.    
    Mostra a Média, Maior, Menor e Situação
    """
    lista = list()
    soma = cont = maior = menor = 0
    for c in range(1, 6):
        lista.append(c)
        soma += c
        cont += 1

        if cont == 1:
            maior = c
            menor = c
        else:
            if cont > maior:
                maior = c
            elif cont < menor:
                menor = c

    media = soma / cont

    if media < 7:
        status = 'REPROVADO'
    else:
        status = 'APROVADO'

    print(lista)
    print(f'Média: {media}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    print(f'Menor: {status}')
    help(notas)


notas()

# Opção 2
def nota(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou ais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['min'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = nota(9, 10, 9, 8.5, sit=True)
print(resp)
help(nota)