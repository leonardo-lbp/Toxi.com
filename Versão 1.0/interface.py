import PySimpleGUI as sg
import os

def tela_inicial(current_directory):
    layout = [
        [sg.Image(filename=current_directory + '/assets/Logo.png')],
        [sg.Text(" ")],
        [sg.Button("Login", key='login_btn', size=(10, 1))],
        [sg.Button("Criar conta", key='criar_btn', size=(10, 1))],
        [sg.Button("Sair", key='sair_btn', size=(10,1))]
    ]
    return layout

def tela_login(current_directory):
    layout = [
        [sg.Column([[sg.Image(filename=current_directory + '/assets/Login.png')]], justification='center')],
        [sg.Text(" ")],
        [sg.Image(filename=current_directory + '/assets/Username.png', pad=(150, 0))],
        [sg.Input(key='username_input', pad=(150, 0))],
        [sg.Image(filename=current_directory + '/assets/Password.png', pad=(150, 0))],
        [sg.Input(key='password_input', password_char='*', pad=(150, 0))],
        [sg.Column([[sg.Button("Entrar", size=(10, 1), key="entrar_btn"), sg.Button("Voltar", size=(10, 1), key="voltar_btn")]], justification='center')]
    ]
    return layout

def tela_crar_conta(current_directory):
    layout = [
        [sg.Column([[sg.Image(filename=current_directory + '/assets/Account_creation.png')]], justification='center')],
        [sg.Text(" ")],
        [sg.Image(filename=current_directory + '/assets/Username.png', pad=(150, 0))],
        [sg.Input(key='username_input', pad=(150, 0))],
        [sg.Image(filename=current_directory + '/assets/Name.png', pad=(150, 0))],
        [sg.Input(key='name_input', pad=(150, 0))],
        [sg.Image(filename=current_directory + '/assets/Password.png', pad=(150, 0))],
        [sg.Input(key='password_input', password_char='*', pad=(150, 0))],
        [sg.Image(filename=current_directory + '/assets/Email.png', pad=(150, 0))],
        [sg.Input(key='email_input', pad=(150,0))],
        [sg.Column([[sg.Button("Criar", size=(10, 1), key="criar_btn")]], justification='center'),
        sg.Column([[sg.Button("Voltar", size=(10, 1), key="voltar_btn")]], justification='center')]
    ]

    return layout

current_directory = os.getcwd()
defaut_element_size = (650, 400)
sg.theme("DarkPurple1")
layout = tela_inicial(current_directory)

janela = sg.Window("Toxi.com", layout, element_justification='center', size=defaut_element_size)

while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED or event == "sair_btn":
        break
    elif event == "login_btn":
        layout = tela_login(current_directory)
        janela.close()
        janela = sg.Window("Toxi.com", layout, size=defaut_element_size)
    elif event == "criar_btn":
        layout = tela_crar_conta(current_directory)
        janela.close()
        janela = sg.Window("Tox.com", layout, size=defaut_element_size)
    elif event == "voltar_btn":
        layout = tela_inicial(current_directory)
        janela.close()
        janela = sg.Window("Toxi.com", layout, element_justification='center', size=defaut_element_size)

janela.close()