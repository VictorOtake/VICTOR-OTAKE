usuario_padrao="admin" 
senha_padrao="admin123" 
usuario_digitado=input("digite um usuario: ") 
senha_digitada= input("digite uma senha: ") 
 
if usuario_digitado==usuario_padrao and senha_digitada==senha_padrao: 
    print("bem-vindo, sucesso") 
else: 
    print("error") 