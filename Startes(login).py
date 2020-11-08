cont = 1
print('\t\t\t\t\tStartses\n\n\nBem vindo')
user1 = str('123')
senha1 = str('123')
vuser1 = str('123')
vsenha1 = str('123')
cuser1 = str('123')
csenha1 = str('123')
while cont>=1:
    tuser=input('Você é um:\nDigite 1 para comprador\nDigite 2 para vendedor\nDigite 3 para colaborador\n')
    if tuser == str('1'):
        cad1=input('Ola comprador, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')
        if cad1 == str('1'):
            user=input('Digite seu nome de usuário:')
            senha=input('Digite seu senha:')
            if user == user1 and senha == senha1:
                break
            else:
                print('Login Invalido')
        elif cad1 == str('2'):
            email1=input('Digite seu email para cadastrar:')
            user1=input(str('Digite um nome de usuario:'))
            senha1=input(str('Digite uma senha:'))
            print('Cadastro realizado')
        else:
            print ('Comando invalido')
    elif tuser == str('2'):
        cad2=input('Ola vendedor, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')
        if cad2 == str('1'):
            user=input('Digite seu nome de usuário:')
            senha=input('Digite seu senha:')
            if user == vuser1 and senha == vsenha1:
                break
            else:
                print('Login Invalido')
        elif cad2 == str('2'):
            email1=input('Digite seu email para cadastrar:')
            vuser1=input('Digite um nome de usuario:')
            vsenha1=input('Digite uma senha:')
        else:
            print ('Comando invalido')
    elif tuser == str('3'):
        cad3=input('Ola colaborador, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')
        if cad3 == str('1'):
            user=input('Digite seu nome de usuário:')
            senha=input('Digite seu senha:')
            if user == cuser1 and senha == csenha1:
                break
            else:
                print('Login Invalido')
        elif cad3 == str('2'):
            email1=input('Digite seu email para cadastrar:')
            cuser1=input('Digite um nome de usuario:')
            csenha1=input('Digite uma senha:')
        else:
            print ('Comando invalido')
    else:
        print ('Comando invalido')
print('login completo')

