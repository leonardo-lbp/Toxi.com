from account import *
from community import *

class Perfil:
    def __init__(self):
        self.accountsList = Account()
        self.communityList = Community()

    def Account_FollowButton(self, accountIndex, profileName):
        if 0 <= accountIndex < len(self.accountsList):
            account = self.accountsList[accountIndex]
            newFollower = {'username': profileName}
            account['follower'].append(newFollower)
        else:
            print("Não achado!!")

    def Account_ShowFollowingAccounts(self, accountIndex):
        if 0 <= accountIndex < len(self.accountsList):
            account = self.accountsList[accountIndex]
            print(f"Seguindo contas ({account['name']}):")
            for follower in account['follower']:
                print(f"  - {follower['username']}")
        else:
            print("Não achado!!")

    def Account_ShowFollowingCommunities(self, accountIndex):
        if 0 <= accountIndex < len(self.accountsList):
            account = self.accountsList[accountIndex]
            print(f"Seguindo comunidades ({account['name']}):")
            for follower in account['follower']:
                print(f"  - {follower['username']}")
        else:
            print("Não achado!!")

    def Community_FollowButton(self, communityIndex, profileName):
        if 0 <= communityIndex < len(self.communityList):
            community = self.communityList[communityIndex]
            newMember = {'username': profileName}
            community['member'].append(newMember)
        else:
            print("Não achado!!")

    def Community_ShowMembers(self, communityIndex):
        if 0 <= communityIndex < len(self.communityList):
            community = self.communityList[communityIndex]
            print(f"Membros da comunidade ({community['name']}):")
            for member in community['member']:
                print(f"  - {member['username']}")
        else:
            print("Não achado!!")
    
    