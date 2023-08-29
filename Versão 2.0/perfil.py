from account import Account
from community import Community
from autentic import autentic
from data import Data
import exception_erros

class Profile:
    def __init__(self):
        self.accounts = Account()
        self.communitys= Community()
        self.user_data = Data("Conta.json")
        self.community_data = Data("Comunidade.json")


    #verifica se o campo de name foi preenchido
    def is_a_valid_name(self, name):
        if len(name) <= 0:
            raise exception_erros.InvalidUserNameError


    #verifica se a senha é valida
    def is_a_valid_password(self, password):
        if autentic.checkpassword(password):
            raise exception_erros.InvalidPasswordError


    #verifica se o email é válido
    def is_a_valid_email(self, email):
        if autentic.checkemail(email):
            raise exception_erros.InvalidEmailError


    #verifica se o username já existe
    def username_exist(self, username):
        if autentic.checkusername(username, self.accounts.users):
            raise exception_erros.InvalidUsernameErro


    #verifica se o name da comunidade já existe
    def name_exist(self, name):
        if autentic.checkcommunityname(name, self.communitys.communitys):
            raise exception_erros.InvalidCommunityNameError


    #verifica o acesso do usuairo
    def acces_verify(self, username, community, access_level):
        if autentic.checkaccess(username, community) != access_level:
            raise exception_erros.InvalidAccessUserError
        
    
    #verifica se o usuario foi encontrado
    def user_is_find(self, user):
        if user == {}:
            raise exception_erros.InvalidUserError
        

    #verifica se a comunidae foi encontrada
    def community_is_find(self, community):
        if community == {}:
            raise exception_erros.InvalidCommunityError
        

    #pega o usuario pelo nome
    def get_user(self, username):
        user = autentic.finduser(username, self.accounts.users)
        self.user_is_find(user)

        return user


    #pega o nome do usuario
    def get_user_name(self, user):
        return user["name"]


    #insere o nome do usuario
    def set_user_name(self, user, new_name):
        self.is_a_valid_name(new_name)
        self.accounts.edit_account_name(new_name, user)


    #pega o username do usuario
    def get_user_username(self, user):
        return user['username']


    #insere o useraneme do usuario
    def set_user_username(self, user, new_username):
        self.username_exist(new_username)
        self.accounts.edit_account_username(new_username, user, self.communitys.communitys)


    #pega a senha do usuario
    def get_user_password(self, user):
        return user["password"]


    #insere a senha do usuario
    def set_user_password(self, user, new_password):
        self.is_a_valid_password(new_password)
        self.accounts.edit_account_password(new_password, user)


    #pega o email do usuario
    def get_user_email(self, user):
        return user["email"]


    #insere o email do usuario
    def set_user_email(self, user, new_email):
        self.is_a_valid_email(new_email)
        self.accounts.edit_account_email(new_email, user)


    #pega a comuniade
    def get_community(self, community_name):
        community = autentic.findcommunity(community_name, self.communitys.communitys)
        self.community_is_find(community)

        return community


    #pega o nome da comunidade
    def get_community_name(self, community):
        return community["name"]

    #insere o nome da comunidae
    def set_community_name(self, community, new_name):
        self.name_exist(new_name)
        self.communitys.edit_name_of_comunity(community, community["name"], new_name, self.accounts.users)


    #pega a descrição da comunidade
    def get_community_description(self, community):
        return community["description"]


    #insere a descrição da comunidade
    def set_community_description(self, community, new_description):
        new_description = new_description.capitalize()
        self.communitys.edit_description_of_community(new_description, community)


    #salva os dados de usuário e de comunidade
    def save_data(self):
        self.user_data.save_data(self.accounts.users)
        self.community_data.save_data(self.communitys.communitys)


    #carrega os dados de usuairo e da comunidade
    def load_data(self):
        self.accounts.users = self.user_data.load_data()
        self.communitys.communitys = self.community_data.load_data()
