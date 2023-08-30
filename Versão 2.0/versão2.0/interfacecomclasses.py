import PySimpleGUI as sg
from Perfil import Profile
import os
import exception_erros

#classe base da interface 
class BaseScreen:
    def __init__(self, window_name, data):
        self.window_size = (900, 450)
        self.back_color = '#3C1642'
        self.window_name = window_name
        self.window = None
        self.layout = []
        self.profile = Profile()
        self.profile = data

    def load_data(self):
        self.profile.load_data()


    def save_data(self):
        self.profile.save_data()


    def create_window(self):
        self.window = sg.Window(self.window_name, self.layout, size=self.window_size, background_color=self.back_color)


    def run(self):
        self.create_window()
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            self.events(event, values)
        self.window.close()


    def close(self):
        if self.window:
            self.window.close()




class LoginScreen(BaseScreen):
    def __init__(self, data):
        super().__init__('Login', data)
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [
                sg.Column([
                    [sg.Text('               TOXI.COM', font=('Helvetica', 22), justification='center', background_color=cor_roxo_escuro)],
                    [sg.Image(filename=logo_path, size=(400, 400), background_color=cor_roxo_escuro)]
                ], background_color=cor_roxo_escuro),
                sg.VSeperator(),
                sg.Column([
                    [sg.Text('Bem vindo(a)', font=('Helvetica', 22), background_color=cor_roxo_escuro)],
                    [sg.Text('Login: ', pad=(8, 8), background_color=cor_roxo_escuro), sg.InputText(key='login')],
                    [sg.Text(key='wrong_username', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Text('Senha:', pad=(8, 8), background_color=cor_roxo_escuro), sg.InputText(key='senha', password_char='*')],
                    [sg.Checkbox('Mostrar senha', key='mostrar_senha', background_color=cor_roxo_escuro, enable_events=True)],
                    [sg.Text(key='wrong_password', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Column([[sg.Button('Entrar', key='login_btn', pad=(10, 10), size=(10,2)), sg.Button('Criar Conta', key='create_btn', pad=(10, 10), size=(10,2))],
                                [sg.Button('Sair', pad=(10, 10), size=(10,2), key='exit_btn')]], element_justification='c', justification='center', background_color=cor_roxo_escuro)]
                ],
                background_color=cor_roxo_escuro, pad=(20, 0))
            ]
        ]


    def events(self, event, value):
        if event == 'mostrar_senha':
            password = value['senha']
            sg.popup(f"Senha: {password}")
            self.window['mostrar_senha'].update(False)

        if event == 'create_btn':
            self.close()
            create_user = UserCreateScreen(self.profile)
            create_user.run()

        if event == 'login_btn':
            try:
                username = value['login']
                password = value['senha']
                self.profile.login_verify(username, password)

                user = self.profile.get_user(username)
                self.close()
                create_user = UserProfileScreen(self.profile, user)
                create_user.run()
            except exception_erros.InvaldLoginError:
                self.window['wrong_username'].update("Username incorreto!")
                self.window['login'].update('')
                self.window['wrong_password'].update("Password incorreto!")
                self.window['senha'].update('')

        if event == 'exit_btn':
            self.close()


class UserCreateScreen(BaseScreen):
    def __init__(self, data):
        super().__init__('Criar Usuario', data)
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [
                sg.Stretch(background_color=cor_roxo_escuro),
                sg.Column([
                    [sg.Text('Criar Conta', font=('Helvetica', 22), background_color=cor_roxo_escuro)],
                    [sg.Text('Login: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='login_criar')],
                    [sg.Text(key='wrong_username', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Text('Senha:', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='senha_criar', password_char='*')],
                    [sg.Text(key='wrong_password', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Text('Nome: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='nome_criar')],
                    [sg.Text(key='wrong_name', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Text('Email: ', pad=(8, 12), background_color=cor_roxo_escuro), sg.InputText(key='email_criar')],
                    [sg.Text(key='wrong_email', size=(60, 1), justification='center', background_color=cor_roxo_escuro, text_color='Red')],
                    [sg.Column([[sg.Checkbox('Mostrar senha', key='mostrar_senha', background_color=cor_roxo_escuro, enable_events=True)],
                    [sg.Button('Criar', pad=(10, 10), size=(10, 2), key='create_btn'), sg.Button('Voltar', pad=(10,10), size=(10, 2), key='back_btn')]], element_justification='c', justification='center', background_color=cor_roxo_escuro)]
                ],
                element_justification='c',
                background_color=cor_roxo_escuro, pad=(20, 0)),
                sg.Stretch(background_color=cor_roxo_escuro)
            ]
        ]


    def events(self, event, value):
        if event == 'mostrar_senha':
            password = value['senha_criar']
            sg.popup(f"Senha: {password}")
            self.window['mostrar_senha'].update(False)

        if event == 'create_btn':
            try:
                name = value['nome_criar']
                password = value['senha_criar']
                username = value['login_criar']
                email = value['email_criar']
                self.window['wrong_name'].update("")
                self.window['wrong_username'].update("")
                self.window['wrong_password'].update("")
                self.window['wrong_email'].update("")



                error_triggered = False

                try:
                    self.profile.is_a_valid_name(name)
                except exception_erros.InvalidUserNameError:
                    self.window['wrong_name'].update("Campo obrigatório!")
                    self.window['nome_criar'].update('')
                    error_triggered = True

                try:
                    self.profile.is_a_valid_password(password)
                except exception_erros.InvalidPasswordError:
                    self.window['wrong_password'].update("Senha inválida")
                    self.window['senha_criar'].update('')
                    error_triggered = True

                try:
                    self.profile.username_exist(username)
                    self.profile.is_a_valid_username(username)
                except exception_erros.InvalidUsernameError2:
                    self.window['wrong_username'].update("Campo obrigatório!")
                    self.window['login_criar'].update('')
                    error_triggered = True
                except exception_erros.InvalidUsernameError:
                    self.window['login_criar'].update('')
                    self.window['wrong_username'].update("Usuário já existe!")
                    error_triggered = True

                try:
                    self.profile.is_a_valid_email(email)
                except exception_erros.InvalidEmailError:
                    self.window['email_criar'].update('')
                    self.window['wrong_email'].update("Email inválido!")
                    error_triggered = True

                if not error_triggered:
                    self.profile.accounts.create_account(username, password, name, email)
                    sg.popup("Conta criada com sucesso!")
                    self.close()
                    login_screen = LoginScreen(self.profile)
                    login_screen.run()

            except:
                pass

        if event == 'back_btn':
            self.close()
            login_screen = LoginScreen(self.profile)
            login_screen.run()



class UserProfileScreen(BaseScreen):
    def __init__(self, data, user):
        super().__init__('Perfil de usuario', data)
        config_path = os.path.join(os.path.dirname(__file__), 'assets', 'config.png')
        createcommunity_path = os.path.join(os.path.dirname(__file__), 'assets', 'comu.png')
        exit_path = os.path.join(os.path.dirname(__file__), 'assets', 'exit.png')
        search_path = os.path.join(os.path.dirname(__file__), 'assets', 'bus.png')
        cor_roxo_escuro = '#3C1642'
        self.user = user
        self.layout = [
            [
                sg.Column(
                    [
                        [sg.Text('Bem vindo(a) ' + user['name'], font=('Helvetica', 20), justification='left', background_color=cor_roxo_escuro)],
                        [sg.Text('', background_color=cor_roxo_escuro)],
                        [sg.Image(filename=search_path, size=(40,40), background_color=cor_roxo_escuro), sg.Button('Buscar', font=('Helvetica', 15), key='search', enable_events=True)],
                        [sg.Image(filename=config_path, size=(40,40), background_color=cor_roxo_escuro), sg.Button('Configurações', font=('Helvetica', 15), key='config', enable_events=True)],
                        [sg.Image(filename=createcommunity_path, size=(40,40), background_color=cor_roxo_escuro), sg.Button('Criar Comunidade', font=('Helvetica', 15), key='communityCreate', enable_events=True)],
                        [sg.Image(filename=exit_path, size=(40,40), background_color=cor_roxo_escuro), sg.Button('Sair', font=('Helvetica', 15), key="exit_btn")],
                        [sg.Text('', size=(0, 10), background_color=cor_roxo_escuro)]
                    ],
                    background_color=cor_roxo_escuro,
                    element_justification='c'
                ),
                sg.VSeparator(),
                sg.Column(
                    [
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text(len(user["followers"]), font=('Helvetica', 10), background_color=cor_roxo_escuro, justification='right')],
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text('Seguidores', font=('Helvetica', 15), background_color=cor_roxo_escuro, key='followers', enable_events=True, justification='right')],
                        [sg.Text('', size=(0, 20),background_color=cor_roxo_escuro)]
                    ],
                    element_justification='c',
                    background_color=cor_roxo_escuro
                ),
                sg.Column(
                    [
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text(len(user["following"]), font=('Helvetica', 10), background_color=cor_roxo_escuro, pad=(10, 0), justification='right')],
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text('seguindo', font=('Helvetica', 15), background_color=cor_roxo_escuro, key='following', enable_events=True, pad=(10, 0), justification='right')],
                        [sg.Text('', size=(0, 20),background_color=cor_roxo_escuro)]
                    ],
                    element_justification='c',
                    background_color=cor_roxo_escuro
                ),
                sg.Column(
                    [
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text(len(user["community"]), font=('Helvetica', 10), background_color=cor_roxo_escuro)],
                        [sg.Text('', size=(5,0), background_color=cor_roxo_escuro), sg.Text('Comunidade', font=('Helvetica', 15), background_color=cor_roxo_escuro, key='com', enable_events=True)],
                        [sg.Text('', size=(0, 20),background_color=cor_roxo_escuro)]
                    ],
                    element_justification='c',
                    background_color=cor_roxo_escuro
                )
            ]
        ]

    def events(self, event, value):
        if event == 'config':
            layout = [
                [sg.Column([
                [sg.Button('Editar conta', key='user_edit')],
                [sg.Button('Deletar conta', key='user_delet')],
                [sg.Button('Voltar', key='back_btn')] 
                ], 
                    justification='center',
                    element_justification='c'
                    )
                ]
            ]
            popup_window = sg.Window('Opções de Configuração', layout)
    
            while True:
                event_popup, values_popup = popup_window.read()
                if event_popup == sg.WIN_CLOSED or event_popup == 'back_btn':
                    break
                elif event_popup == 'user_edit':
                    self.close()
                    edit_screen = EditUserScreen(self.profile, self.user)
                    break
                elif event_popup == 'user_delet':
                    break
            
            popup_window.close()
            edit_screen.run()

        if event == 'com':
            self.close()
            communitys_profile = UserCommunitysScreen(self.profile, self.user)
            communitys_profile.run()
        
        if event == 'exit_btn':
            self.close()
            login_screen = LoginScreen(self.profile)
            login_screen.run()



class EditUserScreen(BaseScreen):
    def __init__(self, data, user):
        super().__init__('Perfil de usuario', data)
        self.user = user
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [sg.Column([
                [sg.Text('Editar conta: ', font=('Helvetica', 20), justification='left', background_color=cor_roxo_escuro)],
                [sg.Button('Editar name', key='name_edit')],
                [sg.Button('Editar username', key='username_edit')],
                [sg.Button('Editar password', key='password_edit')],
                [sg.Button('Editar e-mail', key='email_edit')],
                [sg.Button('Voltar', key='back_btn')]
                ], 
                justification='center',
                background_color=cor_roxo_escuro,
                element_justification='c'
                )
            ]
        ]

    def events(self, event, value):
        if event == 'name_edit':
            layout = [
                [sg.Column([
                [sg.Text('Name: ', pad=(8, 8)), sg.InputText(key='name')],
                [sg.Text(key='wrong_name', size=(60, 1), text_color='Red')],
                [sg.Button('Editar', key='edit_btn')],
                [sg.Button('Voltar', key='back_btn')] 
                ], 
                    justification='center',
                    element_justification='c'
                    )
                ]
            ]
            popup_window = sg.Window('Opções de Configuração', layout)
    
            while True:
                event_popup, values_popup = popup_window.read()
                if event_popup == sg.WIN_CLOSED or event_popup == 'back_btn':
                    break
                elif event_popup == 'edit_btn':
                    old_name = self.profile.get_user_name(self.user)
                    new_name = values_popup['name']
                    popup_window['wrong_name'].update("")
                    try:
                        if old_name == new_name:
                            raise ValueError("O novo nome não pode ser igual ao anterior")
                        self.profile.set_user_name(self.user, new_name)
                    except exception_erros.InvalidUserNameError:
                        popup_window['wrong_name'].update('Campo obrigatório!')
                        popup_window['name'].update('')
                    except ValueError:
                        popup_window['wrong_name'].update('O novo nome não pode ser igual ao anterior!')
                        popup_window['name'].update('')
                    else:
                        sg.popup("Nome editado com sucesso!")
                        popup_window.close()

                elif event_popup == 'back_btn':
                    break
            
            popup_window.close()

        if event == 'username_edit':
            layout = [
                [sg.Column([
                [sg.Text('Username: ', pad=(8, 8)), sg.InputText(key='username')],
                [sg.Text(key='wrong_username', size=(60, 1), text_color='Red')],
                [sg.Button('Editar', key='edit_btn')],
                [sg.Button('Voltar', key='back_btn')] 
                ], 
                    justification='center',
                    element_justification='c'
                    )
                ]
            ]
            popup_window = sg.Window('Opções de Configuração', layout)
    
            while True:
                event_popup, values_popup = popup_window.read()
                if event_popup == sg.WIN_CLOSED or event_popup == 'back_btn':
                    break
                elif event_popup == 'edit_btn':
                    old_username = self.profile.get_user_username(self.user)
                    new_username = values_popup['username']
                    popup_window['wrong_username'].update("")
                    try:
                        if old_username == new_username:
                            raise ValueError("O novo username não pode ser igual ao anterior")
                        self.profile.is_a_valid_username(new_username)
                        self.profile.set_user_username(self.user, new_username)
                    except exception_erros.InvalidUsernameError:
                        popup_window['wrong_username'].update('Este username já existe!')
                        popup_window['username'].update('')
                    except exception_erros.InvalidUsernameError2:
                        popup_window['wrong_username'].update('Campo Obrigatório!')
                        popup_window['username'].update('')
                    except ValueError:
                        popup_window['wrong_username'].update('O novo nome não pode ser igual ao anterior!')
                        popup_window['username'].update('')
                    else:
                        sg.popup("Username editado com sucesso!")
                        popup_window.close()

                elif event_popup == 'back_btn':
                    break
            
            popup_window.close()

        if event == 'back_btn':
            self.close()
            create_user = UserProfileScreen(self.profile, self.user)
            create_user.run()
    
    
class UserCommunitysScreen(BaseScreen):
    def __init__(self, data, user):
        super().__init__('Comunidades do usuario', data)
        self.user = user
        button_layout = [[sg.Button(communityname['name'], size=(20, 1), key=communityname['name'])] for communityname in user['community']]
        cor_roxo_escuro = '#3C1642'
        self.layout = [
            [sg.Column([
                [sg.Text('Seguidores: ', font=('Helvetica', 20), justification='left', background_color=cor_roxo_escuro)],
                [sg.Column(button_layout, scrollable=True, vertical_scroll_only=True, size=(180, 350))],
                [sg.Button('Voltar')]
                ], 
                justification='center',
                background_color=cor_roxo_escuro,
                element_justification='c'
                )
            ]
        ]


if __name__ == "__main__":
    profile = Profile()
    profile.load_data()
    inciar = LoginScreen(profile)
    inciar.run()
    profile.save_data()