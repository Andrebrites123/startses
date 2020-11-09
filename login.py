# Variaveis globais para simulação de um banco de dados
# Cuidado para não mudá-las sem querer. Quando possível, defina
# uma variavel dentro de uma função
esta_logado = False
email = ''
senha = ''
tipo = ''

TIPO_DE_CADASTRO = ['comprador', 'vendedor', 'colaborador']

# Exibe as opções de cadastro ou login
def tela_inicial_menu():
    # Constantes para navegação do usuário
    TELA_COMPRADOR = '1'
    TELA_VENDEDOR = '2'
    TELA_COLABORADOR = '3'
    EH_LOGIN = '1'
    EH_CADASTRO = '2'
    # Fim das contantes de navegação do usuário

    tuser = input('Você é um:\nDigite 1 para comprador\nDigite 2 para vendedor\nDigite 3 para colaborador\n')

    if tuser == TELA_COMPRADOR:
        tipo = TIPO_DE_CADASTRO[0]
        escolha_do_usuario = input('Ola comprador, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')

        if escolha_do_usuario == EH_LOGIN:
            formulario_login()
        elif escolha_do_usuario == EH_CADASTRO:
            if(formulario_cadastro()):
                print('Cadastro realizado')
        else:
            print('Comando invalido')

    elif tuser == TELA_VENDEDOR:
        tipo = TIPO_DE_CADASTRO[1]
        escolha_do_usuario = input('Ola vendedor, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')
        
        if escolha_do_usuario == EH_LOGIN:
            formulario_login()
        elif escolha_do_usuario == EH_CADASTRO:
            if(formulario_cadastro()):
                print('Cadastro realizado')
        else:
            print ('Comando invalido')

    elif tuser == TELA_COLABORADOR:
        tipo = TIPO_DE_CADASTRO[2]
        escolha_do_usuario = input('Ola colaborador, você já possui cadastro?\nDigite 1 para Sim\nDigite 2 para Não\n')

        if escolha_do_usuario == EH_LOGIN:
            formulario_login()
        elif escolha_do_usuario == EH_CADASTRO:
            if(formulario_cadastro()):
                print('Cadastro realizado')
        else:
            print ('Comando invalido')

# Verifica se o email e senha são válidos
def eh_valido(email_preenchido = '', senha_preenchida = ''):
    return ((esta_logado and email and senha) or 
        email and senha and 
        email == email_preenchido and 
        senha == senha_preenchida)

def formulario_cadastro():
    email_preenchido = input('Digite seu email:')
    senha_preenchida = input('Digite seu senha:')
    # TODO se possível, testar se os dados preenchidos são válidos para retornar verdadeiro ou falso
    global email
    global senha
    email = email_preenchido
    senha = senha_preenchida

# Apresenta a tela de login
def formulario_login():
    email_preenchido = input('Digite seu email:')
    senha_preenchida = input('Digite seu senha:')
    
    if(eh_valido(email_preenchido, senha_preenchida)):
        global esta_logado 
        esta_logado = True
        print('login bem sucedido')
    else:
        print('Login inválido')
    
def logout(escolha_do_usuario):
    if(escolha_do_usuario and escolha_do_usuario == 's'):
        global esta_logado
        global email
        global senha
        
        esta_logado = False
        email = ''
        senha = ''