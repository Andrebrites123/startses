import login as login
# Variaveis globais para simulação de um banco de dados
# Cuidados para não mudalalas sem querer, quando possível, defina
# uma variavel dentro de uma função
continuar_rodando = True
vezes_dentro_do_while = 0

print('\t\t\t\t\tStartses\n\n\nBem vindo')

while continuar_rodando:
    if(not login.eh_valido()):
        login.tela_inicial_menu()
    else:
        print('Bem vindo a tela inicial da aplicação')

        deseja_sair = input('Deseja sair da sua conta? [S/N]')
        login.logout(deseja_sair)

    
    sair = input('Sair do programa? [S/N]')
    
    if(sair and sair.upper() == 'S'):
        continuar_rodando = False
        
    vezes_dentro_do_while += 1
        