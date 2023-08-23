from autentic import autentic
from data import data_account

class Account:
    def __init__(self):
        self.users = []

    #cria a conta
    def create_account(self, name, password, username, email):
        #verificando se o username já existe
        if autentic.checkusername(username, self.users):
            print("Este username já existe")
            return
        #verificando se o email é válido
        if autentic.checkemail(email):
            print("Insira um email válido")
            return
        #verificando se o password é valido
        if autentic.checkpassword(password):
            print("Senha inválida")
            return
        
        new_user = {
                "name": name,
                "password": password,
                "username": username,
                "email": email,
                "followers": [],
                "following": [],
                "communitys": []
            }
        self.users.append(new_user)

    #auxilia na edição do nome na lista de seguindo e seguidores 
    def edit_username_in_followersAndfollowing(self, you, f1, f2, youInFriendList, new_username):
        for followingfriends in you[f1]:
                friend = autentic.finduser(followingfriends["username"], self.users)
                for changeyou in friend[f2]:
                    if changeyou["username"] == youInFriendList:
                        changeyou["username"] = new_username
                        break

    #edita a conta
    def edit_account(self, username):
        #pegando o usuario e testando se ele existe
        you = autentic.finduser(username, self.users)
        if you == {}:
            print("Usuario não encontrado")
            return
        
        select_edit = int(input("Insira o que você quer modificar:\n1.Name\n2.Username\n3.Passowrd\n4.E-mail\n"))
        
        #edita o nome
        if select_edit == 1:
            new_name = input("Insira o novo nome: ")
            you["name"] = new_name
        
        #edita o username
        if select_edit == 2:
            new_username = input("Insira o novo username: ")

            if autentic.checkusername(new_username, self.users):
                print("Este username já existe")
                return
            
            youInFriendList = you["username"]
            you["username"] = new_username

            #muda seu usernome na lista seguidos
            self.edit_username_in_followersAndfollowing(you, "following", "followers", youInFriendList, new_username)

            #muda seu username na lista de seguidores
            self.edit_username_in_followersAndfollowing(you, "followers", "following", youInFriendList, new_username)

            #muda seu username nos grupos


    #segue o usuário
    def userfollow(self, youusername, friendusername):
        #verifica se o usuário existe
        you = autentic.finduser(youusername, self.users)
        if you == {}:
            print("Usuário não encontrado")
            return
        
        #verifica se o amigo existe
        friend = autentic.finduser(friendusername, self.users)
        if friend == {}:
            print("Usuario não encontrado")
            return

        #verifica se o usuario que você vai seguir já está sendo seguido
        if autentic.checkusername(friend["username"], you["following"]):
            print("Seguindo")
            return
        
        #adiciona o novo amigo a sua lista de seguindo
        new_friend = {"username": friendusername}
        you["following"].append(new_friend)
        you_follow = {"username": youusername}
        friend["followers"].append(you_follow)

    #retira o seguir do usuario
    def unfollow(self, youusername, friendusername):
        #verifica se o usuário existe
        you = autentic.finduser(youusername, self.users)
        if you == {}:
            print("Usuário não encontrado")
            return
        
        #verifica se o amigo existe
        friend = autentic.finduser(friendusername, self.users)
        if friend == {}:
            print("Usuario não encontrado")
            return

        #verifica se o usuario que você vai deixar de seguir existe na sua lista de seguindo
        if not autentic.checkusername(friend["username"], you["following"]):
            print("Você não segue o usuário")
            return
        
        #remove o usuário da lista de seguindo e você da lista de seguidores do usuário
        remove_you = {"username": you["username"]}
        remove_friend = {"username": friend["username"]}
        friend["followers"].remove(remove_you)
        you["following"].remove(remove_friend)

    #auxilia a deletar seu nome das listas de seguindo e seguidores
    def delet_account_aux(self, you, f1, f2):
        for followingfriends in you[f1]:
                friend = autentic.finduser(followingfriends["username"], self.users)
                for deletyou in friend[f2]:
                    if deletyou["username"] == you["username"]:
                        friend[f2].remove(deletyou)
                        break

    #deleta a conta
    def delet_account(self, username):
        you = autentic.finduser(username, self.users)
        #Verifica se a conta existe
        if you == {}:
            print("Usuário não encontrado")
            return
        
        opc = input("Você realmente deseja deletar a conta?")
        opc = opc.capitalize()

        #deleta a conta
        if opc == "Yes" or opc == "Y" or opc == "Sim" or opc == "S":
            confirmusername = input("Confirme seu username: ")
            confirmpassword = input("Confirme sua senha: ")
            if confirmusername != you["username"] and confirmpassword != you["password"]:
                print("Username ou senha inválidos")
                return
            #remove seu nome da lista de segudos
            self.delet_account_aux(you, "following", "followers")
            
            #remove seu nome da lista de seguidores
            self.delet_account_aux(you, "followers", "following")

            #remove seu nome da lista de grupos
            #exclui sua conta
            self.users.remove(you)





data_user = data_account()
users = Account()
for user in data_user:
    users.create_account(user["name"], user["password"], user["username"], user["email"])

while True:
    opc = int(input("1.criar conta\n2.editar conta\n3.seguir conta\n4.deixar de seguir conta\n5.deletar conta\n6.printar contas\n7.sair\n"))
    if opc == 1:
        name = input("name: ")
        password = input("password: ")
        username = input("username: ")
        email = input("email: ")
        users.create_account(name, password, username, email)
        
    if opc == 2:
        username = input("username: ")
        users.edit_account(username)

    if opc == 3:
        youusername = input("youusername: ")
        friendusername = input("friendusername: ")
        users.userfollow(youusername, friendusername)

    if opc == 4:
        youusername = input("youusername: ")
        friendusername = input("friendusername: ")
        users.unfollow(youusername, friendusername)

    if opc == 5:
        username = input("username: ")
        users.delet_account(username)

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

    if opc == 7:   
        break 