#  5. desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) /2

if media>=6:
    print("Voce esta aprovado")
elif media<=6 and media>=5:
    print("Voce esta de recuperação")
else:
    print("Voce esta reprovado")