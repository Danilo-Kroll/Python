# 011 Faça um programa que leia a largura e a altura de uma parede em metros, caclcule a sua parea e
# quantidade de tinra necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("Informe a largura da parede (m): "))
altura = float(input("Informe a altura da parede (m): "))
valorTinta = float(input("Valor do litro de tinta (R$): "))

area = largura * altura
tinta = area / 2

print("A parede tem dimensão de {:.2f} x {:.2f} e área de {:.2f}m².".format(largura, altura, area))
print("Você precisará de {:.2f}l de tinta.".format(tinta))
print("Valor total da tinta: R${:.2f}.".format(valorTinta * tinta))