from autentic import autentic

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
