nt1=float(input("insira primeira nota: ")) 
nt2=float(input("insira segunda nota: ")) 
nt3=float(input("insira terceira nota: ")) 
media=(nt1+nt2+nt3)/3 
if media>=7: 
    print("aprovado") 
elif media>=5 and media<7: 
    print("recuperação") 
else: 
    print("reprovado")