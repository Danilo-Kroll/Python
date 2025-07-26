# 106 Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

cores = ('\033[m',          # 0 - sem cores
        '\033[0;30;41m',    # 1 - vermelho
        '\033[0;30;42m',    # 2 - verde
        '\033[0;30;43m',    # 3 - amarelo
        '\033[0;30;44m',    # 4 - azul
        '\033[0;30;45m',    # 5 - roxo
        '\033[7;30m'        # 6 - branco
        );


def pyHelp(aju):
    titulo(f'Acessando o manual do comando \'{aju}\'', 4)
    print(cores[6], end='')
    help(aju)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')


ajuda = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    ajuda = str(input("Função ou Biblioteca: "))
    if ajuda.upper() == 'FIM':
        break
    else:
        pyHelp(ajuda)

titulo('ATÉ LOGO!', 1)