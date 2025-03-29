# 7. faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
valor = float(input("Qual o valor do produto: "))
desconto = valor*0.05
prec = valor-desconto
print(f"Desconto de 5% valor do produto de R${valor}  é: R${prec}")
