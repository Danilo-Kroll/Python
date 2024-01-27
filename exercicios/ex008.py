# 008 Escreva um programa que leia um valor em metros e o exiba convertido em
# centimetros e milimetros (km, hm. dam, dm, cm, mm)

m = (int(input("Digite uma distância em metro (m): ")))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print("A medida {} corresponde a : \n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm".format(m, km, hm, dam, dm, cm, mm))