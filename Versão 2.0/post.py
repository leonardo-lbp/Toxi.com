class Posts:
    def __init__(self):
        self.profiles = []
        self.communities = []
    


    def account_access(self, xusername):
        for profile in self.profiles:
            if profile['name'] == xusername:
                posts = profile['posts']
                if len(posts) == 0:
                    print('Não há posts na conta')
                else:
                    print('Posts:')
                    for post in posts:
                        print(f"       {post['writer']}: {post['message']}")
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
                                posts = profile['posts']
                                if len(posts) == 0:
                                    print('Não há posts na comunidade')
                                else:
                                    print('Posts:')
                                    for post in posts:
                                        print(f"       {post['writer']}: {post['post']}")
                        break
        if not community_found:
            print('Você não é admin da comunidade ou a comunidade não existe')


    
    def account_send(self, xusername, xpost):
        for profile in self.profiles:
            if profile['name'] == xusername:
                profile['posts'].append({'writer': xusername, 'post': xpost})
                print('Post publicado com sucesso!')
                break



    def community_send(self, xusername, xcommunity, xpost):
        for community in self.communities:
            if community['name'] == xcommunity:
                is_member = False
                for member in community['member']:
                    if member['username'] == xusername:
                        is_member = True
                        for profile in self.profiles:
                            if profile['name'] == xcommunity:
                                profile['posts'].append({'writer': xusername, 'post': xpost})
                                print('Post publicado com sucesso!')
                                break
            if not is_member:
                print('Você não é membro da comunidade')
            break
        else:
            print('A comunidade não existe')