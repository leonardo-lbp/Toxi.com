import main
import json
import time
import sys
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





#Bloco de funções de manipulação da comunidade
def newCommunity(Cname, Cdescription):
    global communityList
    Cmember = []
    Cadmin = []
    newCommunity = {'name': Cname, 'description': Cdescription, 'member': Cmember, 'admin': Cadmin}
    communityList.append(newCommunity)

def followCommunity(index, username):
    global communityList
    newMember = {'username': username}
    communityList[index]['member'].append(newMember)

def getAdminRights(index, username):
    global communityList
    newAdmin = {'username': username}
    communityList[index]['admin'].append(newAdmin)

def show(communityNumber):
    global communityList
    print('Community', communityNumber)
    thisAcommunityList = communityList[communityNumber]
    print('       Name:', thisAcommunityList['name'])
    print('       Decription:', thisAcommunityList['description'])
    print('       Members:', len(thisAcommunityList['member']))
    print('       Admins: ', len(thisAcommunityList['admin']))
    print()

def is_user_admin(community, username):
    for admin in community['admin']:
        if admin['username'] == username:
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
        print('Pressione A para criar uma comunidade')
        print('Pressione B para excluir uma comunidade')
        print('Pressione C para seguir uma comunidade')
        print('Pressione D para deixar de seguir uma comunidade')
        print('Pressione E para mostrar todas as comunidades')
        print('Pressione F para mostrar seguidores de uma comunidade')
        print('Pressione G para mostrar todos os administradores de uma comunidade')
        print('Pressione H para moderar uma comunidade')
        print('Pressione I para editar uma comunidade')
        print('Pressione Q para voltar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('Oque você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            time.sleep(0.5)
            print('Criação de comunidade:')
            cname = input('Insira o nome da comunidade: ')
            index = 0
            for community in communityList:
                if community['name'] == cname:
                    print('Esse nome de comunidade já está em uso. Por favor, escolha outro nome.')
                    break
                index += 1
            else:
                cdescription = input('Insira a descrição da comunidade: ')
                provLogin = input('Insira seu login: ')
                provPassword = input('Insira sua senha: ')
                for account in accountsList:
                    if account['login'] == provLogin and account['password'] == provPassword:
                        newCommunity(cname, cdescription)
                        newProfile(cname)
                        followCommunity(index, account['name'])
                        getAdminRights(index, account['name'])
                        print('Comunidade criada com sucesso!')
                        break
                else:
                    print('Credenciais inválidas, tente novamente')
                

        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de comunidade:')
            communityName = input('Insira o nome da comunidade que deseja excluir: ')
            community_found = False

            for community in communityList:
                if community['name'] == communityName:
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    provName = None
                    for account in accountsList:
                        if account['login'] == provLogin and account['password'] == provPassword:
                            provName = account['name']
                            if is_user_admin(community, provName) or len(community['member']) == 0:
                                communityList.remove(community)
                                removeProfile(communityName)
                                print('Comunidade excluída com sucesso!')
                                community_found = True
                                break
                            else:
                                print('Você não tem permissão para excluir esta comunidade.')
                                break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
            else:
                if not community_found:
                    print('A comunidade inserida é inválida ou não existe.')


        elif action == 'c':
            time.sleep(0.5)
            print('Seguir comunidade:')
            name = input('Insira o nome da comunidade que deseja seguir: ')
            index = 0
            valid_community = False
            for a in communityList:
                if a['name'] == name:
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            followCommunity(index, b['name'])
                            if len(a['admin']) == 0:
                                getAdminRights(index, b['name'])
                                print('Você se tornou um administrador da comunidade!')
                            print('Comunidade seguida com sucesso!')
                            valid_community = True
                            break
                index += 1
            if not valid_community:
                print('Nome inválido, tente novamente')


        elif action == 'd':
            time.sleep(0.5)
            print('Deixar de seguir uma comunidade:')
            communityName = input('Insira o nome da comunidade que deseja deixar de seguir: ')
            account_found = False
            community_found = False
            for community in communityList:
                if community['name'] == communityName:
                    community_found = True
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            for member in community['member']:
                                if member['username'] == b['name']:
                                    if is_user_admin(community, b['name']):
                                        community['admin'] = [admin for admin in community['admin'] if admin['username'] != b['name']]
                                    community['member'].remove(member)
                                    print('Deixou de seguir a comunidade com sucesso!')
                                    account_found = True
                                    break
                    break
            if not community_found:
                print('O nome da comunidade inserida é inválido, tente novamente')
            elif not account_found:
                print('Você não é um membro desta comunidade ou suas credenciais são inválidas.')

        
        elif action == 'e':
            time.sleep(0.5)
            print('Lista de comunidades:')
            nCommunity = len(communityList)
            if nCommunity == 0:
                print('Não existem comunidades criadas no momento!')
            else:
                for aCommunityNumber in range(0, nCommunity):
                    show(aCommunityNumber)


        elif action == 'f':
            time.sleep(0.5)
            print('Mostrar membros:')
            name = input('Insira o nome da comunidade que deseja exibir membros: ')
            community_found = False
            for community in communityList:
                if community['name'] == name:
                    community_found = True
                    num_members = len(community['member'])
                    if num_members == 0:
                        print('Esta comunidade não possui membros!')
                    else:
                        for member_index in range(num_members):
                            print(f'       Member ({member_index}): {community["member"][member_index]["username"]}')
                    break
            if not community_found:
                print('Nome de comunidade inválido, tente novamente')


        elif action == 'g':
            time.sleep(0.5)
            print('Mostrar administradores:')
            name = input('Insira o nome da comunidade que deseja exibir administradores: ')
            community_found = False
            for community in communityList:
                if community['name'] == name:
                    community_found = True
                    num_admins = len(community['admin'])
                    if num_admins == 0:
                        print('Esta comunidade não possui administradores!')
                    else:
                        for admin_index in range(num_admins):
                            print(f'       Admin ({admin_index}): {community["admin"][admin_index]["username"]}')
                    break
            if not community_found:
                print('Nome de comunidade inválido, tente novamente')


        elif action == 'h':
            time.sleep(0.5)
            print('Moderação de comunidade:')
            name = input('Insira o nome da comunidade que deseja moderar: ')
            community_found = False
            for community in communityList:
                if community['name'] == name:
                    community_found = True
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for account in accountsList:
                        if account['login'] == provLogin and account['password'] == provPassword:
                            provName = account['name']
                            if is_user_admin(community, provName):
                                print(f'Você é um administrador da comunidade "{name}"')
                                print('Escolha o que deseja fazer:')
                                print('     1. Tornar um usuário da comunidade um administrador')
                                print('     2. Renunciar ao cargo de administrador')
                                print('     3. Excluir um membro da comunidade')
                                field_choice = int(input('Opção: '))
                                if field_choice == 1:
                                    username = input('Insira o nome do usuário que deseja tornar administrador: ')
                                    for member in community['member']:
                                        if member['username'] == username:
                                            if is_user_admin(community, username):
                                                print(f'{username} já é um administrador da comunidade.')
                                            else:
                                                getAdminRights(communityList.index(community), username)
                                                print(f'{username} agora é um administrador da comunidade.')
                                            break
                                    else:
                                        print('Usuário não encontrado na comunidade.')
                                elif field_choice == 2:
                                    if len(community['admin']) == 1:
                                        print('Você é o único administrador, não pode renunciar ao cargo.')
                                    else:
                                        community['admin'] = [admin for admin in community['admin'] if admin['username'] != provName]
                                        print(f'{provName} renunciou ao cargo de administrador.')
                                elif field_choice == 3:
                                    username = input('Insira o nome do usuário que deseja excluir da comunidade: ')
                                    for member in community['member']:
                                        if member['username'] == username:
                                            if is_user_admin(community, username):
                                                print('Você não pode excluir um administrador da comunidade.')
                                            else:
                                                community['member'] = [m for m in community['member'] if m['username'] != username]
                                                print(f'{username} foi excluído da comunidade.')
                                                if is_user_admin(community, username):
                                                    community['admin'] = [admin for admin in community['admin'] if admin['username'] != username]
                                            break
                                    else:
                                        print('Usuário não encontrado na comunidade.')
                                else:
                                    print('Opção inválida, tente novamente')
                            else:
                                print('Você não é um administrador desta comunidade.')
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
            if not community_found:
                print('Nome de comunidade inválido, tente novamente')

        
        elif action == 'i':
            time.sleep(0.5)
            print('Editar comunidade:')
            communityName = input('Insira o nome da comunidade que deseja editar: ')
            community_found = False
            for community in communityList:
                if community['name'] == communityName:
                    community_found = True
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for account in accountsList:
                        if account['login'] == provLogin and account['password'] == provPassword:
                            provName = account['name']
                            if is_user_admin(community, provName):
                                print(f'Você é um administrador da comunidade "{communityName}"')
                                print('Escolha o que deseja editar:')
                                print('     1. Nome da comunidade')
                                print('     2. Descrição da comunidade')
                                field_choice = int(input('Opção: '))
                                if field_choice == 1:
                                    newCname = input('Insira o novo nome da comunidade: ')
                                    oldCname = community['name']
                                    community['name'] = newCname
                                    updateProfileUsername(oldCname, newCname)
                                    print('Nome da comunidade editado com sucesso!')
                                elif field_choice == 2:
                                    newCdescription = input('Insira a nova descrição da comunidade: ')
                                    community['description'] = newCdescription
                                    print('Descrição da comunidade editada com sucesso!')
                                else:
                                    print('Opção inválida, tente novamente')
                            else:
                                print('Você não é um administrador desta comunidade.')
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
            if not community_found:
                print('A comunidade inserida é inválida ou não existe.')


        elif action == 'q':
            main.menu()


        elif action == 'x':
            time.sleep(0.5)
            print('Programa fechado!')
            sys.exit()


        else:
            print('Opção inválida, tente novamente!')
        

        time.sleep(0.5)
        saveChanges('Comunidade.json', communityList)
        saveChanges('Perfil.json', profileList)

print('Done')


if __name__ == '__main__':
    operations()
