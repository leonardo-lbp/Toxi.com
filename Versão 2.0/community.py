from autentic import autentic

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
