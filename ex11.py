novo_login=input("digite seu email para cadastro: ") 
novo_login=novo_login.lower() 
nova_senha=input("digite a senha desejada: ") 
tamanho_senha=len(nova_senha) 
if tamanho_senha>8: 
    print("reinicie o processo, a senha deve ter no máximo que 8 caracteres.") 
else: 
    print("email e senha cadastrado com sucesso!") 
    print("faça o login com os dados recem cadastrados") 
    login=input("insira seu email: ") 
    senha=input("insira senha cadastrada: ") 
    if novo_login==login and nova_senha==senha: 
        print("bem vindo") 
    else: 
        print("login ou senha invalido, tente novamente")