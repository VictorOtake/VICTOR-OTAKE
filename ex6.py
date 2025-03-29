#6. faça um programa que leia um número inteiro qualquer e mostre sua tabuada
num1 = int(input('digite um valor'))
contador = 0
while contador <10:
    contador+=1
    print(f"{num1} X {contador} = {num1*contador}")