import json
import time
import main
import sys
profileList = []
accountsList = []




#Bloco de funções de manipulação do perfil
def newProfile(pName):
    global profileList
    pMessages = []
    pPosts = []
    newProfile = {'name': pName, 'messages': pMessages, 'posts': pPosts}
    profileList.append(newProfile)

def addMessage(index, writer, message):
    global profileList
    newMessage = {'writer': writer, 'message': message}
    profileList[index]['messages'].append(newMessage)

def addPost(index, writer, message):
    global profileList
    newPost = {'writer': writer, 'message': message}
    profileList[index]['posts'].append(newPost)

def search_profile():
    global accountsList, communityList, profileList

    profileName = input('Digite o perfil que deseja acessar: ')
    found_profile = None

    for profile in profileList:
        if profile['name'] == profileName:
            found_profile = profile
            break
    if not found_profile:
        print('Perfil não encontrado')
        return

    provLogin = input('Digite o login: ')
    provPassword = input('Digite a senha: ')
    is_account_profile = False
    for account in accountsList:
        if account['login'] == provLogin and account['password'] == provPassword:
            provName = account['name']
            is_account_profile = True
            follower_found = False
            for follower in account['follower']:
                if follower['username'] == profileName:
                    follower_found = True
                    break
            if follower_found:
                print()
            else:
                print('Você não segue esse perfil')
                return
            break
    else:
        print('Credenciais inválidas')
        return

    is_community_profile = False
    if not is_account_profile:
        for community in communityList:
            if community['name'] == profileName:
                is_community_profile = True
                member_found = False
                for member in community['member']:
                    if member['username'] == provName:
                        member_found = True
                        break
                if member_found:
                    print()
                else:
                    print('Você não é membro dessa comunidade')
                    return
                break

    if not is_account_profile and not is_community_profile:
        print('Erro: Perfil encontrado não é de uma conta nem de uma comunidade')
        return
    
    if not is_community_profile:
        posts = found_profile['posts']
        if len(posts) == 0:
            print('Não há posts no mural')
        else:
            print('||' , found_profile['name'] , '||')
            print('Followers: ', len(account['follower']))
            print('Posts:')
            for post in posts:
                print(f"       {post['writer']}: {post['message']}")
                print()
    
    elif not is_account_profile:
        posts = found_profile['posts']
        if len(posts) == 0:
            print('Não há posts no mural')
        else:
            print('||' , found_profile['name'] , '||')
            print('Description:' , community['description'])
            print('Posts:')
            for post in posts:
                print(f"       {post['writer']}: {post['message']}")
                print()




#Bloco de funções de manipulação da conta
def newAccount(aLogin, aPassword, aName, aEmail):
    global accountsList
    aFollower = []
    newAccountDict = {'login': aLogin, 'password': aPassword, 'name': aName, 'email': aEmail, 'follower': aFollower}
    accountsList.append(newAccountDict)

def followAccount(index, name):
    global accountsList
    newMember = {'name': name}
    accountsList[index]['follower'].append(newMember)




#Bloco de funções de manipulação da comunidade
def is_user_admin(community, username):
    for admin in community['admin']:
        if admin['username'] == username:
            return True
    return False

def is_user_member(community, username):
    for member in community['member']:
        if member['username'] == username:
            return True
    return False




#Bloco de funções de manipulação txt
def saveChanges(data, list):
    with open(data, "w") as file:
        json.dump(list, file, indent=2)

def loadFromJSON(archive):
    global accountsList, communityList, profileList
    try:
        with open(archive, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    return data




#Função de operações
def operations():
    while True:
        global accountsList, communityList, profileList
        accountsList = loadFromJSON('Conta.json')
        communityList = loadFromJSON('Comunidade.json')
        profileList = loadFromJSON('Perfil.json')

        print()
        print()
        print('Pressiona A para acessar suas mensagens')
        print('Pressione B para enviar uma mensagem')
        print('Pressione C para acessar seus posts')
        print('Pressione D para fazer um post')
        print('Pressione E para buscar um perfil')
        print('Pressione Q para voltar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('Oque você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            time.sleep(0.5)
            print('Caixa de mensagens:')
            print('Ver caixa de mensagens de uma conta ou de uma comunidade? ')
            print('     1. Conta')
            print('     2. Comunidade')
            field_choice = int(input('Opção: '))
            if field_choice == 1:
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                nAccounts = len(accountsList)
                account_found = False
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        account_found = True
                        nProfiles = len(profileList)
                        for profileNumber in range(nProfiles):
                            if profileList[profileNumber]['name'] == accountsList[accountNumber]['name']:
                                messages = profileList[profileNumber]['messages']
                                if len(messages) == 0:
                                    print('Não há mensagens na comunidade')
                                else:
                                    print('Messages:')
                                    for message in messages:
                                        print(f"       {message['writer']}: {message['message']}")
                else:
                    if not account_found:
                        print('Credenciais inválidas. Não foi possível acessar as mensagens')

            elif field_choice == 2:
                community_name = input('Qual o nome da comunidade? ')
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                community_found = False
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        nCommunities = len(communityList)
                        for communityNumber in range(nCommunities):
                            if communityList[communityNumber]['name'] == community_name and is_user_admin(communityList[communityNumber], accountsList[accountNumber]['name']):
                                community_found = True
                                nProfiles = len(profileList)
                                for profileNumber in range(nProfiles):
                                    if profileList[profileNumber]['name'] == community_name:
                                        messages = profileList[profileNumber]['messages']
                                        if len(messages) == 0:
                                            print('Não há mensagens na comunidade')
                                        else:
                                            print('Messages:')
                                            for message in messages:
                                                print(f"       {message['writer']}: {message['message']}")
                        else:
                            if not community_found:
                                print('Você não é admin da comunidade ou a comunidade não existe')
                        break
                else:
                    print('Credenciais inválidas')
            
            else:
                print('Opção inválida.')

        
        elif action == 'b':
            time.sleep(0.5)
            print('Enviar mensagem:')
            print('Enviar mensagem como uma conta ou como uma comunidade? ')
            print('     1. Conta')
            print('     2. Comunidade')
            field_choice = int(input('Opção: '))

            if field_choice == 1:
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        recipient_name = input('Para quem deseja enviar a mensagem? ')
                        message_text = input('Digite a mensagem que deseja enviar: ')
                        recipient_found = False
                        for profileNumber, profile in enumerate(profileList):
                            if profile['name'] == recipient_name:
                                addMessage(profileNumber, accountsList[accountNumber]['name'], message_text)
                                print('Mensagem enviada com sucesso!')
                                recipient_found = True
                                break
                        if not recipient_found:
                            print('Destinatário não encontrado')
                        break
                else:
                    print('Credenciais inválidas')

            elif field_choice == 2:
                community_name = input('Qual o nome da comunidade? ')
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                community_found = False
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        nCommunities = len(communityList)
                        for communityNumber in range(nCommunities):
                            if communityList[communityNumber]['name'] == community_name and is_user_admin(communityList[communityNumber], accountsList[accountNumber]['name']):
                                community_found = True
                                break
                        else:
                            if not community_found:
                                print('Você não é admin da comunidade ou a comunidade não existe')
                        break
                else:
                    print('Credenciais inválidas')
                if not community_found:
                    continue

                recipient_name = input('Para quem deseja enviar a mensagem? ')
                recipient_found = False
                for profileNumber, profile in enumerate(profileList):
                    if profile['name'] == recipient_name:
                        addMessage(profileNumber, accountsList[accountNumber]['name'], input('Digite a mensagem que deseja enviar: '))
                        print('Mensagem enviada com sucesso!')
                        recipient_found = True
                        break

                if not recipient_found:
                    print('Destinatário não encontrado')

            else:
                print('Opção inválida.')


        elif action == 'c':
            time.sleep(0.5)
            print('Mural de posts:')
            print('Ver o mural de sua conta ou de uma comunidade que faz parte? ')
            print('     1. Conta')
            print('     2. Comunidade')
            field_choice = int(input('Opção: '))
            if field_choice == 1:
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                nAccounts = len(accountsList)
                account_found = False
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        account_found = True
                        nProfiles = len(profileList)
                        for profileNumber in range(nProfiles):
                            if profileList[profileNumber]['name'] == accountsList[accountNumber]['name']:
                                posts = profileList[profileNumber]['posts']
                                if len(posts) == 0:
                                    print('Não há posts no mural')
                                else:
                                    print()
                                    print('Posts', '(' , accountsList[accountNumber]['name'] , ')' , ':')
                                    print()
                                    for post in posts:
                                        print(f"       {post['writer']}: {post['message']}")
                                        print()
                else:
                    if not account_found:
                        print('Credenciais inválidas. Não foi possível acessar os posts')

            elif field_choice == 2:
                community_name = input('Qual o nome da comunidade? ')
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                community_found = False
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        nCommunities = len(communityList)
                        for communityNumber in range(nCommunities):
                            if communityList[communityNumber]['name'] == community_name and is_user_member(communityList[communityNumber], accountsList[accountNumber]['name']):
                                community_found = True
                                nProfiles = len(profileList)
                                for profileNumber in range(nProfiles):
                                    if profileList[profileNumber]['name'] == community_name:
                                        posts = profileList[profileNumber]['posts']
                                        if len(posts) == 0:
                                            print('Não há posts no mural')
                                        else:
                                            print()
                                            print('Posts', '(' , community_name , ')' , ':')
                                            print()
                                            for post in posts:
                                                print(f"       {post['writer']}: {post['message']}")
                                                print()
                        else:
                            if not community_found:
                                print('Você não é membro da comunidade ou a comunidade não existe')
                        break
                else:
                    print('Credenciais inválidas')

            else:
                print('Opção inválida.')


        elif action == 'd':
            time.sleep(0.5)
            print('Fazer um post:')
            print('Fazer um post em sua conta ou em uma comunidade que faz parte? ')
            print('     1. Conta')
            print('     2. Comunidade')
            field_choice = int(input('Opção: '))

            if field_choice == 1:
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        addPost(accountNumber, accountsList[accountNumber]['name'], input('Digite o post que deseja enviar: '))
                        print('Post feito com sucesso!')
                        break
                else:
                    print('Credenciais inválidas')

            elif field_choice == 2:
                community_name = input('Qual o nome da comunidade? ')
                provLogin = input('Qual seu login? ')
                provPassword = input('Qual sua senha? ')
                community_found = False
                nAccounts = len(accountsList)
                for accountNumber in range(nAccounts):
                    if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                        nCommunities = len(communityList)
                        for communityNumber in range(nCommunities):
                            if communityList[communityNumber]['name'] == community_name and is_user_member(communityList[communityNumber], accountsList[accountNumber]['name']):
                                community_found = True
                                addPost(communityNumber, accountsList[accountNumber]['name'], input('Digite o post que deseja enviar: '))
                                print('Post feito com sucesso!')
                                break
                        else:
                            if not community_found:
                                print('Você não é membro da comunidade ou a comunidade não existe')
                        break
                else:
                    print('Credenciais inválidas')

            else:
                print('Opção inválida.')
        

        elif action == 'e':
            time.sleep(0.5)
            print('Buscar perfil:')
            search_profile()


        elif action == 'q':
            main.menu()


        elif action == 'x':
            time.sleep(0.5)
            print('Programa fechado!')
            sys.exit()


        else:
            print('Opção inválida, tente novamente!')

        
        time.sleep(0.5)
        saveChanges('Perfil.json', profileList)


if __name__ == '_main_':
    operations()