import os
import PySimpleGUI as sg

def tela_busca():
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'busca.png')
    cor_roxo_escuro = '#3C1642'
    layout = [
        [
            sg.Column([
                [sg.Image(filename=icon_path, size=(34, 34), background_color=cor_roxo_escuro)]
            ], background_color=cor_roxo_escuro),
            sg.VSeperator(),  # Linha vertical
            sg.Column([
                [sg.Text('', background_color=cor_roxo_escuro), sg.InputText(key='busca')],
            ], background_color=cor_roxo_escuro)
        ]
    ]
    return layout


def tela_mensagem():
    message_path = os.path.join(os.path.dirname(__file__), 'assets', 'mensagem.png')
    cor_roxo_escuro = '#3C1642'
    layout = [
        [
            sg.Image(filename=message_path, size=(34, 34), background_color=cor_roxo_escuro),
            sg.Text('|  Caixa de Mensagens', font=('Helvetica', 18), background_color=cor_roxo_escuro, pad=(10, 0))
        ],
    ]

    """
    # messages é o import do JSON de mensagens (Perfil.json) do usuário que voce validou e guardou o name no momento do login
    for message in messages:
        layout.append([sg.Text(message)])
    """

    return layout


def tela_config():
    config_path = os.path.join(os.path.dirname(__file__), 'assets', 'configurações.png')
    cor_roxo_escuro = '#3C1642'
    layout = [
        [
            sg.Image(filename=config_path, size=(40, 40), background_color=cor_roxo_escuro),
            sg.Text('|  Configurações', font=('Helvetica', 22), background_color=cor_roxo_escuro, pad=(10, 0), text_color='#000000'),
        ],
        [
            [sg.Text('', font=('Helvetica', 18), background_color=cor_roxo_escuro, pad=(10, 0))],
            [sg.Text('Editar conta', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10))],
            [sg.Text('Excluir conta', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10))],
            [sg.Text('Editar comunidade', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10))],
            [sg.Text('Excluir comunidade', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10))]
        ]
    ]
    return layout



# Criando a janela
layout = tela_config()
cor_roxo_escuro = '#3C1642'
window = sg.Window('Tela', layout, size=(900, 450), background_color=cor_roxo_escuro)
window.finalize()



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break