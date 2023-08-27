from autentic import autentic
from data import data_community_whit_user
from data import data_user_whit_community

class Account:
    def __init__(self):
        self.users = []


    #cria a conta
    def create_account(self, name, password, username, email):
        new_user = {
                "name": name,
                "password": password,
                "username": username,
                "email": email,
                "followers": [],
                "following": [],
                "community": []
            }
        self.users.append(new_user)

    
    #edita o nome da conta
    def edit_account_name(self, new_name, user):
        user["name"] = new_name


    #edita o username da conta
    def edit_account_username(self, new_username, user, community):
        #edita o usernome da conta na lista de seguidores
        for friend in user["followers"]:
            friend_in_follower = autentic.finduser(friend["username"], self.users)
            edityouusername = autentic.finduser(user["username"], friend_in_follower["following"])
            edityouusername["username"] = new_username

        #edita o username da conta na lista de seguidos
        for friend in user["following"]:
            friend_in_follower = autentic.finduser(friend["username"], self.users)
            edityouusername = autentic.finduser(user["username"], friend_in_follower["followers"])
            edityouusername["username"] = new_username

        #edita o username da conta na lista de comunidades
        for community_edit in user["community"]:
            community_to_edit = autentic.findcommunity(community_edit["name"], community)
            edityouusername = autentic.finduser(user["username"], community_to_edit["member"])
            edityouusername["username"] = new_username

        user["username"] = new_username

    
    #edita a senha
    def edit_account_password(self, new_password, user):
        user["password"] = new_password

    
    #edita o email
    def edit_account_email(self, new_email, user):
        user["email"] = new_email


    #segue o usuário
    def userfollow(self, you, friend):
        you_follow = {"username": you["username"]}
        new_friend = {"username": friend["username"]}
        friend["followers"].append(you_follow)
        you["following"].append(new_friend)


    #retira o seguir do usuario
    def unfollow(self, you, friend):
        remove_you = {"username": you["username"]}
        remove_friend = {"username": friend["username"]}
        friend["followers"].remove(remove_you)
        you["following"].remove(remove_friend)


    #deleta a conta
    def delet_account(self, you, communitys):
        #deleta o usuario da lista de seguidores
        for friend in you["followers"]:
            friend_in_follower = autentic.finduser(friend["username"], self.users)
            remove_user = autentic.finduser(you["username"], friend_in_follower["following"])
            friend_in_follower["following"].remove(remove_user)

        #delta o usuario da lista de seguidos
        for friend in you["following"]:
            friend_in_follower = autentic.finduser(friend["username"], self.users)
            remove_user = autentic.finduser(you["username"], friend_in_follower["followers"])
            friend_in_follower["followers"].remove(remove_user)

        #deleta o usuario da lista de comunidades
        for community_remove in you["community"]:
            community_to_remove = autentic.findcommunity(community_remove["name"], communitys)
            remove_user_in_community = autentic.finduser(you["username"], community_to_remove["member"])
            community_to_remove["member"].remove(remove_user_in_community)

            if len(community_to_remove["member"]) > 0:
                if remove_user_in_community["access"] == 0:
                    for new_creator in community_to_remove["member"]:
                        if new_creator["access"] < high_access:
                            new_creator_in_community = new_creator
                            high_access = new_creator["access"]
                
                new_creator_in_community["access"] = 0
            else:
                communitys.remove(community_to_remove)

        self.users.remove(you)




users = Account()
users.users = data_user_whit_community()
communitys = data_community_whit_user()


while True:
    opc = int(input("1.criar conta\n2.editar conta\n3.seguir conta\n4.deixar de seguir conta\n5.deletar conta\n6.printar contas\n7.printar comunidades\n8.sair\n"))
    #criar
    if opc == 1:
        name = input("name: ")
        password = input("password: ")
        username = input("username: ")
        email = input("email: ")

        #verificando se o username já existe
        if autentic.checkusername(username, users.users):
            print("Este username já existe")
            break
        #verificando se o email é válido
        if autentic.checkemail(email):
            print("Insira um email válido")
            break
        #verificando se o password é valido
        if autentic.checkpassword(password):
            print("Senha inválida")
            break
        
        users.create_account(name, password, username, email)

    #editar    
    if opc == 2:
        username = input("username: ")
        edit_user = autentic.finduser(username, users.users)
        if edit_user == {}:
            print("Usuario não encontrado")
            break
    
        select_edit = int(input("Insira o que você quer modificar:\n1.Name\n2.Username\n3.Passowrd\n4.E-mail\n"))
        
        #edita o nome
        if select_edit == 1:
            new_name = input("Insira o novo nome: ")

            users.edit_account_name(new_name, edit_user)
        
        #edita o username
        if select_edit == 2:
            new_username = input("Insira o novo username: ")
            
            if autentic.checkusername(new_username, users.users):
                print("Este username já existe")
                break

            users.edit_account_username(new_username, edit_user, communitys)

        #edita a senha
        if select_edit == 3:
            new_password = input("Insira a nova senha: ")

            if autentic.checkpassword(new_password):
                print("Senha inválida")
                break
            
            users.edit_account_password(new_password, edit_user)
            
        #edita o email
        if select_edit == 4:
            new_email = input("Insira o novo email: ")

            if autentic.checkemail(new_password):
                print("Senha inválida")
                break
            
            users.edit_account_email(new_email, edit_user)

    #seguir
    if opc == 3:
        youusername = input("youusername: ")
        friendusername = input("friendusername: ")
        #verifica se o usuário existe
        you = autentic.finduser(youusername, users.users)
        if you == {}:
            print("Usuário não encontrado")
            break
        
        #verifica se o amigo existe
        friend = autentic.finduser(friendusername, users.users)
        if friend == {}:
            print("Usuario não encontrado")
            break

        #verifica se o usuario que você vai seguir já está sendo seguido
        if autentic.checkusername(friend["username"], you["following"]):
            print("Seguindo")
            break

        users.userfollow(you, friend)

    #deixar de seguir
    if opc == 4:
        youusername = input("youusername: ")
        friendusername = input("friendusername: ")
        #verifica se o usuário existe
        you = autentic.finduser(youusername, users.users)
        if you == {}:
            print("Usuário não encontrado")
            break
        
        #verifica se o amigo existe
        friend = autentic.finduser(friendusername, users.users)
        if friend == {}:
            print("Usuario não encontrado")
            break

        #verifica se o usuario que você vai deixar de seguir existe na sua lista de seguindo
        if not autentic.checkusername(friend["username"], you["following"]):
            print("Você não segue o usuário")
            break
        
        users.unfollow(you, friend)

    #deletar conta
    if opc == 5:
        username = input("username: ")
        
        you = autentic.finduser(username, users.users)
        #Verifica se a conta existe
        if you == {}:
            print("Usuário não encontrado")
            break
        
        opc = input("Você realmente deseja deletar a conta?")
        opc = opc.capitalize()

        #deleta a conta
        if opc == "Yes" or opc == "Y" or opc == "Sim" or opc == "S":
            confirmusername = input("Confirme seu username: ")
            confirmpassword = input("Confirme sua senha: ")
            if confirmusername != you["username"] and confirmpassword != you["password"]:
                print("Username ou senha inválidos")
                break

            users.delet_account(you, communitys)

    #printar contas
    if opc == 6:
        for user in users.users:
            print("Name: " + user["name"])
            print("Password: " + user["password"])
            print("Username: " + user["username"])
            print("Email: " + user["email"])
            print("Followers:")
            print(user["followers"])
            print("Following:")
            print(user["following"])
            print("Community:")
            print(user["community"])

    #printar comunidade
    if opc == 7:
        for community in communitys:
            print("Name: " + community["name"])
            print("Descriptio: " + community["description"])
            print("Members:")
            print(community["member"])
            print("Banned:")
            print(community["banned"])

    #sair
    if opc == 8:   
        break 
