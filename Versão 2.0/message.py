class Messages:
    def __init__(self):
        self.profiles = []
        self.communities = []
    


    def account_access(self, xusername):
        for profile in self.profiles:
            if profile['name'] == xusername:
                messages = profile['messages']
                if len(messages) == 0:
                    print('Não há mensagens na conta')
                else:
                    print('Messages:')
                    for message in messages:
                        print(f"       {message['writer']}: {message['message']}")
                break



    def community_access(self, xusername, xcommunity):
        community_found = False
        for community in self.communities:
            if community['name'] == xcommunity:
                for admin in community['admin']:
                    if admin['username'] == xusername:
                        community_found = True
                        for profile in self.profiles:
                            if profile['name'] == xcommunity:
                                messages = profile['messages']
                                if len(messages) == 0:
                                    print('Não há mensagens na comunidade')
                                else:
                                    print('Messages:')
                                    for message in messages:
                                        print(f"       {message['writer']}: {message['message']}")
                        break
        if not community_found:
            print('Você não é admin da comunidade ou a comunidade não existe')
    


    def account_send(self, xusername, xrecipient, xmessage):
        for profile in self.profiles:
            if profile['name'] == xusername:
                recipient_found = False
                for recipient in self.profiles:
                    if recipient['name'] == xrecipient:
                        recipient['messages'].append({'writer': xusername, 'message': xmessage})
                        print('Mensagem enviada com sucesso!')
                        recipient_found = True
                        break
                if not recipient_found:
                    print('Destinatário não encontrado')
                break



    def community_send(self, xusername, xcommunity, xrecipient, xmessage):
        for community in self.communities:
            if community['name'] == xcommunity:
                is_admin = False
                for admin in community['admin']:
                    if admin['username'] == xusername:
                        is_admin = True
                        recipient_found = False
                        for recipient in self.profiles:
                            if recipient['name'] == xrecipient:
                                recipient['messages'].append({'writer': xusername, 'message': xmessage})
                                print('Mensagem enviada com sucesso!')
                                recipient_found = True
                                break
                        if not recipient_found:
                            print('Destinatário não encontrado')
                        break
                if not is_admin:
                    print('Você não é admin da comunidade')
                break
        else:
            print('A comunidade não existe')