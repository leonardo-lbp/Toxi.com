import os
import PySimpleGUI as sg

class Search(BaseScreen):
    def __init__(self):
        super().__init__(window_size=(900, 450), back_color='#3C1642', window_name='Buscar')
        search_path = os.path.join(os.path.dirname(__file__), 'assets', 'busca.png')
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [
                sg.Column([
                    [sg.Image(filename=search_path, size=(34, 34), background_color=cor_roxo_escuro)]
                ], background_color=cor_roxo_escuro),
                sg.VSeperator(),  # Linha vertical
                sg.Column([
                    [sg.Text('', background_color=cor_roxo_escuro), sg.InputText(key='busca')]
                ], background_color=cor_roxo_escuro, key='search_in'),
                sg.Column([
                    [sg.Button('Buscar', pad=(10,10), key='search_btn')],
                ], background_color=cor_roxo_escuro)
            ]
        ]

        def events(self, event):
            if event == 'search_btn':
                try:





class Messages(BaseScreen):
    def __init__(self):
        super().__init__(window_size=(900, 450), back_color='#3C1642', window_name='Mensagens')
        message_path = os.path.join(os.path.dirname(__file__), 'assets', 'mensagem.png')
        cor_roxo_escuro = '#3C1642'
        self.layout = [
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


class Config(BaseScreen):
    def __init__(self):
        super().__init__(window_size=(900, 450), back_color='#3C1642', window_name='Configurações')
        config_path = os.path.join(os.path.dirname(__file__), 'assets', 'configurações.png')
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [
                sg.Image(filename=config_path, size=(40, 40), background_color=cor_roxo_escuro),
                sg.Text('|  Configurações', font=('Helvetica', 22), background_color=cor_roxo_escuro, pad=(10, 0), text_color='#000000'),
            ],
            [
                [sg.Text('', font=('Helvetica', 18), background_color=cor_roxo_escuro, pad=(10, 0))],
                [sg.Text('Editar conta', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10), key='edit_account_btn')],
                [sg.Text('Excluir conta', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10), key='exclude_account_btn')],
                [sg.Text('Editar comunidade', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10), key='edit_community_btn')],
                [sg.Text('Excluir comunidade', font=('Helvetica', 15), background_color=cor_roxo_escuro, pad=(10, 10), key='exclude_community_btn')]
            ]
        ]