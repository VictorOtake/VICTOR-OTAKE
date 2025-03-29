num1=float(input("Insira o primeir valor: ")) 
num2=float(input("Insira o segundo valor: ")) 
i=input("Coloque um operador para fazer o calculo dos 2 valores: + , - , /, *: ")
if i=='+': 
    print(f"O soma dos dois valores é: {num1+num2}") 
elif i=='-': 
    print(f"O subtração dos dois valores é: {num1-num2}") 
elif i=='/': 
    print(f"O divisao dos dois valores é: {num1/num2}") 
elif i=='*': 
    print(f"O multipicação dos dois valores é: {num1*num2}")