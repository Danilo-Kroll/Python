# 058 Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint

escolha = randint(0, 10)

num = 0

tentativa = 0

while num != escolha:
	num = int(input("Escolha um número: "))
	tentativa += 1
	if num > escolha:
		print("Menos... Tente novamente!")
	if num < escolha:
		print("Mais... Tente novamente!")
print("VOCÊ ACERTOU DEPOIS DE {} TENTATIVAS!! O número escolhido pelo computador foi {}, e você escolheu {}.".format(tentativa, escolha, num))