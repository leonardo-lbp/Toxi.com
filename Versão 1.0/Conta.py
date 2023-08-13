import main
import re
import json
import time
import sys
profileList = []
communityList = []
accountsList = []




#Bloco de funções de manipulação do perfil
def newProfile(pName):
    global profileList
    pMessages = []
    pPosts = []
    newProfile = {'name': pName, 'messages': pMessages, 'posts': pPosts}
    profileList.append(newProfile)

def removeProfile(profile_name):
    global profileList
    profileList = [profile for profile in profileList if profile['name'] != profile_name]

def updateProfileUsername(oldUsername, newUsername):
    global profileList
    for profile in profileList:
        if profile['name'] == oldUsername:
            profile['name'] = newUsername




# Bloco de funções de manipulação da conta
def newAccount(aLogin, aPassword, aName, aEmail):
    global accountsList
    aFollower = []
    newAccountDict = {'login': aLogin, 'password': aPassword, 'name': aName, 'email': aEmail, 'follower': aFollower}
    accountsList.append(newAccountDict)

def followAccount(index, name):
    global accountsList
    newMember = {'username': name}
    accountsList[index]['follower'].append(newMember)

def editAccount(accountNumber, field, newValue):
    global accountsList
    accountsList[accountNumber][field] = newValue

def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Login:', thisAccountDict['login'])
    print('       Password:', thisAccountDict['password'])
    print('       Name:', thisAccountDict['name'])
    print('       Email:', thisAccountDict['email'])
    print('       Followers:', len(thisAccountDict['follower']))
    print()

def removeAccountFromFollowers(username):
    global accountsList
    for account in accountsList:
        account['follower'] = [follower for follower in account['follower'] if follower['username'] != username]

def removeAccountFromMembers(username):
    global communityList
    for community in communityList:
        community['member'] = [member for member in community['member'] if member['username'] != username]

def removeAccountFromAdmins(username):
    global communityList
    for community in communityList:
        community['admin'] = [admin for admin in community['admin'] if admin['username'] != username]

def updateUsernameInFollowers(oldUsername, newUsername):
    global accountsList
    for account in accountsList:
        for follower in account['follower']:
            if follower['username'] == oldUsername:
                follower['username'] = newUsername

def updateUsernameInMembers(oldUsername, newUsername):
    global communityList
    for community in communityList:
        for member in community['member']:
            if member['username'] == oldUsername:
                member['username'] = newUsername

def updateUsernameInAdmins(oldUsername, newUsername):
    global communityList
    for community in communityList:
        for admin in community['admin']:
            if admin['username'] == oldUsername:
                admin['username'] = newUsername




# Bloco de funções de manipulação txt
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




# Função de operações
def operations():
    while True:
        global accountsList, communityList, profileList
        accountsList = loadFromJSON('Conta.json')
        communityList = loadFromJSON('Comunidade.json')
        profileList = loadFromJSON('Perfil.json')

        print()
        print()
        print('Pressione A para criar uma conta')
        print('Pressione B para excluir uma conta')
        print('Pressione C para seguir uma conta')
        print('Pressione D para deixar de seguir uma conta')
        print('Pressione E para mostrar todas as contas')
        print('Pressione F para mostrar os seguidores de uma conta')
        print('Pressione G para mostrar quem uma conta segue')
        print('Pressione H para editar uma conta')
        print('Pressione Q para voltar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('O que você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            time.sleep(0.5)
            print('Nova conta:')
            userLogin = input('Qual será seu login? ')
            for a in accountsList:
                if a['login'] == userLogin:
                    print('Esse login já está em uso, tente novamente')
                    break
            else:
                userPassword = input('Qual será sua senha(mínimo 6 dígitos)? ')
                while len(userPassword) < 6:
                    userPassword = input('Senha muito pequena! Tente novamente: ')
                userName = input('Qual será seu username? ')
                for b in accountsList:
                    if b['name'] == userName:
                        print('Esse username já está em uso, tente novamente')
                        break
                else:
                    default_email = r'^[a-zA-Z0-9._%+=#]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9].+$'
                    userEmail = input('Qual será seu email? ')
                    while not re.match(default_email, userEmail):
                        userEmail = input('Email incorreto! Insira um Email válido: ')
                    for c in accountsList:
                        if c['email'] == userEmail:
                            print('Esse email já está em uso, tente novamente')
                            break
                    else:
                        newAccount(userLogin, userPassword, userName, userEmail)
                        newProfile(userName)
                        print('Conta criada com sucesso!')


        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de conta:')
            provLogin = input('Insira seu login: ')
            provPassword = input('Insira sua senha: ')
            removed_accounts = []
            for a in accountsList:
                if a['login'] == provLogin and a['password'] == provPassword:
                    removed_accounts.append(a['name'])
                    accountsList.remove(a)
                    removeAccountFromFollowers(a['name'])
                    removeAccountFromMembers(a['name'])
                    removeAccountFromAdmins(a['name'])
                    removeProfile(a['name'])
                    print('Conta excluída com sucesso!')
                    break
            else:
                print('Credenciais inválidas. Não foi possível excluir a conta.')


        elif action == 'c':
            time.sleep(0.5)
            print('Seguir conta:')
            provName = input('Insira o username da conta que deseja seguir: ')
            index = 0
            account_found = False
            for a in accountsList:
                if a['name'] == provName:
                    provLogin = input('Insira seu login: ')
                    provPass = input('Insira sua senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPass:
                            follower_names = [follower['username'] for follower in a['follower']]
                            if b['name'] in follower_names:
                                print('Você já está seguindo essa conta.')
                            else:
                                a['follower'].append({'username': b['name']})
                                print('Seguido com sucesso!')
                            account_found = True
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
                index += 1
            if not account_found:
                print('O username inserido é inválido, tente novamente')


        elif action == 'd':
            time.sleep(0.5)
            print('Deixar de seguir uma conta:')
            provName = input('Insira o username da conta que deseja deixar de seguir: ')
            index = 0
            account_found = False
            for a in accountsList:
                if a['name'] == provName:
                    provLogin = input('Insira seu Login: ')
                    provPass = input('Insira sua Senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPass:
                            follower_names = [follower['username'] for follower in a['follower']]
                            if b['name'] not in follower_names:
                                print('Você não está seguindo essa conta.')
                            else:
                                a['follower'] = [follower for follower in a['follower'] if follower['username'] != b['name']]
                                print('Deixou de seguir com sucesso!')
                            account_found = True
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
                index += 1
            if not account_found:
                print('O username inserido é inválido, tente novamente')


        elif action == 'e':
            time.sleep(0.5)
            print('Lista de Contas:')
            nAccounts = len(accountsList)
            if nAccounts == 0:
                print('Não existem contas criadas no momento!')
            else:
                for accountNumber in range(nAccounts):
                    show(accountNumber)


        elif action == 'f':
            time.sleep(0.5)
            print('Mostrar seguidores:')
            provLogin = input('Insira seu login: ')
            provPassword = input('Insira sua senha: ')
            for a in accountsList:
                if a['login'] == provLogin and a['password'] == provPassword:
                    follower_names = [follower['username'] for follower in a['follower']]
                    if not follower_names:
                        print('Essa conta não possui seguidores!')
                    else:
                        print('Seguidores:')
                        for index, follower_name in enumerate(follower_names):
                            print(f'       Follower ({index}): {follower_name}')
                    break
            else:
                print('Credenciais inválidas, não foi possível exibir os seguidores.')


        elif action == 'g':
            time.sleep(0.5)
            print('Contas que você segue:')
            provLogin = input('Insira seu login: ')
            provPassword = input('Insira sua senha: ')
            for account in accountsList:
                if account['login'] == provLogin and account['password'] == provPassword:
                    user_followed_accounts = [follower['username'] for follower in account['follower']]
                    if not user_followed_accounts:
                        print('Você não está seguindo nenhuma conta.')
                    else:
                        print('Contas seguidas por você:')
                        for index, followed_account in enumerate(user_followed_accounts):
                            print(f'       Following ({index}): {followed_account}')
                    break
            else:
                print('Credenciais inválidas. Não foi possível verificar as contas que você segue.')


        elif action == 'h':
            time.sleep(0.5)
            print('Edição de conta:')
            provLogin = input('Qual seu login? ')
            provPassword = input('Qual sua senha? ')
            nAccounts = len(accountsList)
            for accountNumber in range(nAccounts):
                if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == provPassword:
                    print('Escolha o campo que deseja editar:')
                    print('     1. Login')
                    print('     2. Senha')
                    print('     3. Username')
                    print('     4. Email')
                    field_choice = int(input('Opção: '))
                    if field_choice == 1:
                        new_login = input('Digite o novo login: ')
                        for a in accountsList:
                            if a['login'] == new_login:
                                print('Esse login já está em uso, tente novamente')
                                break
                        else:
                            editAccount(accountNumber, 'login', new_login)
                            print('Login alterado com sucesso!')
                    elif field_choice == 2:
                        new_password = input('Digite a nova senha: ')
                        while len(new_password) < 6:
                            new_password = input('Senha muito pequena! Tente novamente: ')
                        editAccount(accountNumber, 'password', new_password)
                        print('Senha alterada com sucesso!')
                    elif field_choice == 3:
                        new_name = input('Digite o novo username: ')
                        for b in accountsList:
                            if b['name'] == new_name:
                                print('Esse username já está em uso, tente novamente')
                                break
                        else:
                            old_username = accountsList[accountNumber]['name']
                            editAccount(accountNumber, 'name', new_name)
                            updateProfileUsername(old_username, new_name)
                            updateUsernameInFollowers(old_username, new_name)
                            updateUsernameInMembers(old_username, new_name)
                            updateUsernameInAdmins(old_username, new_name)
                            print('Username alterado com sucesso!')
                    elif field_choice == 4:
                        default_email = r'^[a-zA-Z0-9._%+=#]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9].+$'
                        new_email = input('Qual será seu email? ')
                        while not re.match(default_email, new_email):
                            new_email = input('E-mail incorreto! Insira um E-mail válido: ')
                        for c in accountsList:
                            if c['email'] == new_email:
                                print('Esse email já está em uso, tente novamente')
                                break
                        else:
                            editAccount(accountNumber, 'email', new_email)
                            print('Email alterado com sucesso!')
                    else:
                        print('Opção inválida.')
                    break
            else:
                print('Credenciais inválidas. Não foi possível editar a conta.')


        elif action == 'q':
            main.menu()


        elif action == 'x':
            time.sleep(0.5)
            print('Programa fechado!')
            sys.exit()


        time.sleep(0.5)
        saveChanges('Conta.json', accountsList)
        saveChanges('Comunidade.json', communityList)
        saveChanges('Perfil.json', profileList)

print('Done')


if __name__ == '__main__':
    operations()
