import os
import PySimpleGUI as sg
import data
from autentic import autentic
from account import Account



def show_warning(message):
    sg.popup(message, title='', keep_on_top=True)



def tela_login():
    logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
    cor_roxo_escuro = '#3C1642'
    layout = [
        [
            sg.Column([
                [sg.Text('               TOXI.COM', font=('Helvetica', 22), justification='center', background_color=cor_roxo_escuro)],
                [sg.Image(filename=logo_path, size=(400, 400), background_color=cor_roxo_escuro)]
            ], background_color=cor_roxo_escuro),
            sg.VSeperator(),  # Linha vertical
            sg.Column([
                [sg.Text('Bem vindo(a)', font=('Helvetica', 22), background_color=cor_roxo_escuro)],
                [sg.Text('Login: ', pad=(8, 8), background_color=cor_roxo_escuro), sg.InputText(key='login')],
                [sg.Text('Senha:', pad=(8, 8), background_color=cor_roxo_escuro), sg.InputText(key='senha', password_char='*')],
                [sg.Button('Entrar', pad=(10, 10)), sg.Button('Criar Conta', pad=(10, 10))]
            ], background_color=cor_roxo_escuro, pad=(20, 0))
        ]
    ]
    return layout



def tela_criar():
    cor_roxo_escuro = '#3C1642'
    layout = [
        [
            sg.Column([
                [sg.Text('Criar Conta', font=('Helvetica', 22), background_color=cor_roxo_escuro)],
                [sg.Text('Login: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='login_criar')],
                [sg.Text('Senha:', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='senha_criar', password_char='*')],
                [sg.Text('Nome: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='nome_criar')],
                [sg.Text('Email: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='email_criar')],
                [sg.Button('Criar', pad=(10, 10)), sg.Button('Sair', pad=(10,10))]
            ], background_color=cor_roxo_escuro, pad=(20, 0))
        ]
    ]
    return layout



def tela_inicio():
    p1_path = os.path.join(os.path.dirname(__file__), 'assets', 'p1.png')
    p2_path = os.path.join(os.path.dirname(__file__), 'assets', 'p2.png')
    p3_path = os.path.join(os.path.dirname(__file__), 'assets', 'p3.png')
    cor_roxo_escuro = '#3C1642'
    cor_branca = '#FFFFFF'
    layout = [
        [
            sg.Column([
                [sg.Text('Comunidades ', font=('Helvetica', 18), background_color=cor_roxo_escuro)],
            ], background_color=cor_roxo_escuro),
            sg.Column([
                [sg.Text('                          Novidades                             ', font=('Helvetica', 18), text_color='#000000', background_color=cor_branca)],
                [sg.Image(filename=p1_path, size=(500, 150), background_color=cor_roxo_escuro)],
                [sg.Image(filename=p2_path, size=(500, 150), background_color=cor_roxo_escuro)],
                [sg.Image(filename=p3_path, size=(500, 150), background_color=cor_roxo_escuro)]
            ], background_color=cor_roxo_escuro),
            sg.Column([
                [sg.Text('  TOXI.COM', font=('Helvetica', 18), background_color=cor_roxo_escuro)],
            ], background_color=cor_roxo_escuro),
        ]
    ]
    return layout



# Criando a janela
layout = tela_login()
cor_roxo_escuro = '#3C1642'
window = sg.Window('Tela de Login', layout, size=(900, 450), background_color=cor_roxo_escuro)
window.finalize()



# Loop para ler os eventos
while True:
    event, values = window.read()


    if event == sg.WIN_CLOSED:
        break


    elif event == 'Entrar':
        login_input = values['login']
        senha_input = values['senha']
            
        checklist = data.data_account()
            
        if autentic.login(login_input, senha_input, checklist):
            show_warning('Login feito com sucesso')
            layout = tela_inicio()
            window.close()
            window = sg.Window('Inicio', layout, size=(900, 520), background_color=cor_roxo_escuro)
        else:
            show_warning('Login falhou')
            layout = tela_login()
            window.close()
            window = sg.Window('Tela de Login', layout, size=(900, 450), background_color=cor_roxo_escuro)


    elif event == 'Criar Conta':
        layout = tela_criar()
        window.close()
        window = sg.Window('Criar Conta', layout, size=(900, 450), background_color=cor_roxo_escuro)


    elif event == 'Criar':
        login_input = values['login_criar']
        senha_input = values['senha_criar']
        name_input = values['nome_criar']
        email_input = values['email_criar']
            
        checklist = data.data_account()
        new_account = Account()

        if new_account.create_account(name_input, senha_input, login_input, email_input) == 1:
            show_warning('Conta criada com sucesso')
            layout = tela_login()
            window.close()
            window = sg.Window('Criar Conta', layout, size=(900, 450), background_color=cor_roxo_escuro)
        else:
            show_warning('Criação de conta falhou')
            layout = tela_criar()
            window.close()
            window = sg.Window('Criar Conta', layout, size=(900, 450), background_color=cor_roxo_escuro)
    

    elif event == 'Sair':
        layout = tela_login()
        window.close()
        window = sg.Window('Criar Conta', layout, size=(900, 450), background_color=cor_roxo_escuro)


# Fechando a janela
window.close()