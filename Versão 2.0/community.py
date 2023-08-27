from autentic import autentic
from data import data_community_whit_user
from data import data_user_whit_community

class Community:
    #inicia a classe
    def __init__(self):
        self.communitys = []


    #cria a comunidade
    def create_community(self, name, description, admin):
        new_community = {
            "name": name,
            "description": description,
            "member": [{"username": admin["username"], "access": 0}],
            "banned":[]
        }

        self.communitys.append(new_community)

        new_community_for_user = {"name": name}
        admin["community"].append(new_community_for_user)

    
    #edita o nome da comunidade
    def edit_name_of_comunity(self, youcommunity, name, new_name, userList):
        for user in youcommunity["member"]:
                user_edit = autentic.finduser(user["username"], userList)
                for community_edit in user_edit["community"]:
                    if community_edit["name"] == name:
                        community_edit["name"] = new_name
                        break

        youcommunity["name"] = new_name


    #edita a descrição da comunidade
    def edit_description_of_community(self, new_description, youcommunity):
        new_description = new_description.capitalize()
        youcommunity["description"] = new_description


    #muda o nível de acesso do usuario
    def change_member_office(self, admin_user, member_of_community, office):
        if member_of_community["access"] == 0 or admin_user["access"] > 1:
            print("Acesso negado")
            return
        
        if office != 0 and office != 1 and office != 2:
            print("Nível de acesso inválido")
            return
        
        member_of_community["access"] = office


    #bane e desbane o usuario
    def ban_user(self, admin_user, member_of_community, community_moderate, opc, userInuserlist):
        if member_of_community["access"] == 0 or admin_user["access"] > 1 or admin_user["access"] < 0:
            print("Acesso negado")
            return
        
        #bane o usuario
        if opc == 1:
            remove_community = {"name": community_moderate["name"]}
            member_of_community["access"] = -1
            community_moderate["member"].remove(member_of_community)
            userInuserlist["community"].remove(remove_community)
            community_moderate["banned"].append(member_of_community)
            
        #desbane o usuario
        if opc == 2:
            community_moderate["banned"].remove(member_of_community)


    #segue a comunidadde
    def followCommunity(self, userInuserlist, community):
        new_member = {"username": userInuserlist["username"], "access": 2}
        new_community = {"name": community["name"]}
        community["member"].append(new_member)
        userInuserlist["community"].append(new_community)


    #retira o seguir do usuario
    def unfollowcommunity(self, userInuserlist, community, userIncommunity):
        high_access = 3
        delet_member = autentic.finduser(userInuserlist["username"], community["member"])
        delet_community = autentic.findcommunity(community["name"], userInuserlist["community"])

        community["member"].remove(delet_member)
        userInuserlist["community"].remove(delet_community)

        if len(community["member"]) > 0:
            if userIncommunity["access"] == 0:
                for new_creator in community["member"]:
                    if new_creator["access"] < high_access:
                        new_creator_in_community = new_creator
                        high_access = new_creator["access"]
                
                new_creator_in_community["access"] = 0
        else:
            self.communitys.remove(community)


    #deleta a conta
    def deletcommunity(self, userlist, community):
        for user in userlist:
            if autentic.checkcommunityname(community["name"], user["community"]):
                remove_community = autentic.findcommunity(community["name"], user["community"])
                print(remove_community)
                user["community"].remove(remove_community)

        self.communitys.remove(community)





communitys = Community()
users = data_user_whit_community()
communitys.communitys = data_community_whit_user()

while True:
    opc = int(input("1.criar comunidade\n2.editar comunidade\n3.seguir comunidade\n4.deixar de seguir comunidade\n5.deletar comunidade\n6.printar comunidades\n7.sair\n9.moderar a comunidade\n"))
    #criar
    if opc == 1:
        name = input("name: ")
        #checa se já existe uma comunidade com o mesmo nome
        if autentic.checkcommunityname(name, communitys.communitys):
            print("Já existe uma comunidade com este nome")
            break
        description = input("descriptio: ")
        admin = input("admin: ")
        creator_user = autentic.finduser(admin, users)
        if creator_user == {}:
            print("usuario nao encontrado")
            break
        communitys.create_community(name, description, creator_user)

    #editar
    if opc == 2:
        name = input("name: ")
        youcommunity = autentic.findcommunity(name, communitys.communitys)
        #verifica se a comunidade existe
        if youcommunity == {}:
            print("comunidade não encontrada!")
            break

        admin_name = input("admin name: ")
        if autentic.checkaccess(admin_name, youcommunity) < 0 or autentic.checkaccess(admin_name, youcommunity) > 1:
            print("Você não tem autorização para fazer mudanças na comunidade")
            break

        select_edit = int(input("Insira o que você quer modificar:\n1.Name\n2.Description\n"))

        #edita o nome da comunidade
        if select_edit == 1:
            new_name = input("Novo nome: ")
            if autentic.checkcommunityname(new_name, communitys.communitys):
                print("já existe uma comunidade com este nome!")
                break
            
            communitys.edit_name_of_comunity(youcommunity, name, new_name, users)

        #edita a descrição da comunidade
        if select_edit == 2:
            new_description = input("nova descrição: ")
            
            communitys.edit_description_of_community(new_description, youcommunity)
        

    #seguir
    if opc == 3:
        yourname = input("username: ")
        userInuserlist = autentic.finduser(yourname, users)
        if userInuserlist == {}:
            print("usuario não encontrado")
            break
        
        community_name = input("nome da comunidade: ")
        community_for_follow = autentic.findcommunity(community_name, communitys.communitys)
        if community_for_follow == {}:
            print("comunidade não encontrada")
            break

        communitys.followCommunity(userInuserlist, community_for_follow)

    #deseguir
    if opc == 4:
        yourname = input("username: ")
        userInuserlist = autentic.finduser(yourname, users)
        if userInuserlist == {}:
            print("usuario não encontrado")
            break
        
        community_name = input("nome da comunidade: ")
        community_for_unfollow = autentic.findcommunity(community_name, communitys.communitys)
        if community_for_unfollow == {}:
            print("comunidade não encontrada")
            break

        userIncommunity = autentic.finduser(yourname, community_for_unfollow["member"])
        if userIncommunity == {}:
            print("o usuario não existe na comunidade")
            break


        communitys.unfollowcommunity(userInuserlist, community_for_unfollow, userIncommunity)

    if opc == 5:
        community_name = input("nome da comunidade: ")
        community_delet = autentic.findcommunity(community_name, communitys.communitys)
        if community_delet == {}:
            print("comunidade não encontrada")
            break


        communitys.deletcommunity(users, community_delet)

    #printar comunidade
    if opc == 6:
        for community in communitys.communitys:
            print("Name: " + community["name"])
            print("Descriptio: " + community["description"])
            print("Members:")
            print(community["member"])
            print("Banned:")
            print(community["banned"])

    #sair
    if opc == 7:   
        break 

    #printar o usuario
    if opc == 8:
        for user in users:
            print("Name: " + user["name"])
            print("Password: " + user["password"])
            print("Username: " + user["username"])
            print("Email: " + user["email"])
            print("Followers:")
            print(user["followers"])
            print("Following:")
            print(user["following"])
            print("Communitys: ")
            print(user["community"])

    #moderar
    if opc == 9:
        admin_username = input("admin username: ")
        #verifica se o usuario existe
        if not autentic.checkusername(admin_username, users):
            print("usuario nao encontrado")
            break

        community_name = input("community name: ")
        community_moderate = autentic.findcommunity(community_name, communitys.communitys)
        #verifica se a comunidade existe
        if community_moderate == {}:
            print("comunidade não encotrada")
            break

        admin_in_community = autentic.finduser(admin_username, community_moderate["member"])
        #verifica se o usuario e membro e se ele tem acesso
        if admin_in_community == {} or admin_in_community["access"] < 0 or admin_in_community["access"] > 1:
            print("Acesso inválido")
            break

        select_opc = int(input("O que você deseja fazer:\n1.Modificar o nível de acesso do usuario\n2.Banir usuario\n3.Desbanir usuario\n"))

        #muda o nível de acesso do usuario
        if select_opc == 1:
            member_name = input("Insira o nome do membro que você deseja fazer a alteração: ")

            member_of_community = autentic.finduser(member_name, community_moderate["member"])
            
            #checa se o membro existe na comunidade
            if member_of_community == {}:
                print("Este membro não foi encontrado")
                break
            
            office_select = int(input("Cargos:\n0.criador\n1.Admin\n2.Membro\n"))

            communitys.change_member_office(admin_in_community, member_of_community, office_select)
        
        #bane um usuario
        if select_opc == 2:
            member_name = input("Insira o nome do membro que você deseja fazer a alteração: ")

            member_in_userlist = autentic.finduser(member_name, users)

            member_of_community = autentic.finduser(member_name, community_moderate["member"])
            
            #checa se o membro existe na comunidade
            if not autentic.checkusername(member_name, community_moderate["member"]):
                print("Este membro não foi encontrado")
                break
            
            #checa se a comunidade está disponível para o usuario
            if not autentic.checkcommunityname(community_moderate["name"], member_in_userlist["community"]):
                print("este membro não está na comunidade")
                break
            
            communitys.ban_user(admin_in_community, member_of_community, community_moderate, 1, member_in_userlist)

        #desbane o usuario
        if select_opc == 3:
            member_name = input("Insira o nome do membro que você deseja fazer a alteração: ")

            member_in_userlist = autentic.finduser(member_name, users)

            member_of_community = autentic.finduser(member_name, community_moderate["banned"])
            
            #checa se o membro existe na comunidade
            if not autentic.checkusername(member_name, community_moderate["banned"]):
                print("Este membro não foi encontrado")
                break
            
            #checa se a comunidade está disponível para o usuario
            if autentic.checkcommunityname(community_moderate["name"], member_in_userlist["community"]):
                print("este membro não está banido")
                break
            
            communitys.ban_user(admin_in_community, member_of_community, community_moderate, 2, member_in_userlist)
