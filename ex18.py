salario_base=float(input("Qual seu salario base: ")) 
hora_extra=int(input("Qual foi suas horas extras: ")) 
pag_extra=(float(input("Qual o valor pago por hora extra: "))) 
basecalculo=hora_extra*pag_extra 
total= salario_base+basecalculo 
print(f"O valor total com salario base e hora extra é: {total}")