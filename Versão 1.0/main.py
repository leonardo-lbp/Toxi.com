import time
import Conta
import Perfil
import Comunidade
import sys

def menu():    
    print(' ____                                                                 __                                          \n/\  _`\                                              __              /\ \                                         \n\ \ \L\ \     __     ___ ___                __  __  /\_\     ___     \_\ \     ___                 __       ___   \n \ \  _ <\'  /\'__`\ /\' __` __`\             /\ \/\ \ \/\ \  /\' _ `\   /\'_` \   / __`\             /\'__`\    / __`\ \n  \ \ \L\ \/\  __/ /\ \/\ \/\ \            \ \ \_/ | \ \ \ /\ \/\ \ /\ \L\ \ /\ \L\ \           /\ \L\.\_ /\ \L\ \\\n   \ \____/\ \____\\\ \_\ \_\ \_\            \ \___/   \ \_\\\ \_\ \_\\\ \___,_\\\ \____/           \ \__/.\_\\\ \____/\n    \/___/  \/____/ \/_/\/_/\/_/             \/__/     \/_/ \/_/\/_/ \/__,_ / \/___/             \/__/\/_/ \/___/ \n                                                                                                                  ')
    print(' ______    _____       __   __      ______          ____       _____                \n/\__  _\  /\  __`\    /\ \ /\ \    /\__  _\        /\  _`\    /\  __`\     /\'\_/`\  \n\/_/\ \/  \ \ \/\ \   \ `\`\/\'/\'   \/_/\ \/        \ \ \/\_\  \ \ \/\ \   /\      \\\n   \ \ \   \ \ \ \ \   `\/ > <        \ \ \         \ \ \/_/_  \ \ \ \ \  \ \ \__\ \\\n    \ \ \   \ \ \_\ \     \/\'/\`\      \_\ \__  __   \ \ \L\ \  \ \ \_\ \  \ \ \_/\ \ \n     \ \_\   \ \_____\    /\_\\\ \_\    /\_____\/\_\   \ \____/   \ \_____\  \ \_\\\ \_\\\n      \/_/    \/_____/    \/_/ \/_/    \/_____/\/_/    \/___/     \/_____/   \/_/ \/_/\n')
    while True:
        print()
        print('Pressione A para acessar a seção de contas')
        print('Pressione B para acessar a seção de comunidades')
        print('Pressione C para acessar a seção de perfis')
        print('Pressione X para sair')
        print()

        action = input('O que você deseja fazer? ')
        action = action.lower()
        action = action[0]

        if action == 'a':
            time.sleep(0.5)
            print()
            print()
            print('BEM VINDO A SEÇÃO DE CONTAS')
            Conta.operations()

        elif action == 'b':
            time.sleep(0.5)
            print()
            print()
            print('BEM VINDO A SEÇÃO DE COMUNIDADES')
            Comunidade.operations()

        elif action == 'c':
            time.sleep(0.5)
            print()
            print()
            print('BEM VINDO A SEÇÃO DE PERFIS')
            Perfil.operations()

        elif action == 'x':
            print('Programa fechado!')
            sys.exit()

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    menu()
