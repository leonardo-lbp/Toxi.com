import PySimpleGUI as sg
import os
from data import Data
data_users = Data('Conta.json')
users = data_users.load_data()
usercommunity = users[0]
button_layout = [[sg.Button(communityname['name'], size=(20, 1), key=communityname['name'])] for communityname in usercommunity['community']]
cor_roxo_escuro = '#3C1642'
layout = [
    [sg.Column([
        [sg.Text('Seguidores: ', font=('Helvetica', 20), justification='left', background_color=cor_roxo_escuro)],
        [sg.Column(button_layout, scrollable=True, vertical_scroll_only=True, size=(180, 400))],
        [sg.Button('Voltar')]
        ], 
        justification='center',
        background_color=cor_roxo_escuro,
        element_justification='c'
        )
    ]
]

window = sg.Window('Exemplo de Barra de Scroll', layout, background_color=cor_roxo_escuro, size=(900, 450))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    for user in users:
        if event == user['username']:
            print(f'Clicou no botão do usuário: {event}')

window.close()
