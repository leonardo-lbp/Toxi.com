    #usuarios
def data_account():
    data_base = [
        {
            "name": "jose",
            "password": "Mm@1234",
            "username": "jose_l",
            "email": "jose@gmail.com"
        },
        {
            "name": "maria",
            "password": "Mm@1234",
            "username": "maria_l",
            "email": "maria@gmail.com"
        },
        {
            "name": "leo",
            "password": "@leo14M",
            "username": "leonardo2004",
            "email": "leozin@gmail.com"
        },
        {
            "name": "matheus",
            "password": "@Arcanjos00",
            "username": "mat",
            "email": "mat@gmail.com"
        },
        {
            "name": "lua roxa",
            "password": "Pacoca@14",
            "username": "lua roxa00",
            "email": "luaRoxa@gmail.com"
        },
        {
            "name": "maca verde",
            "password": "macaVerde045@",
            "username": "maca verde00",
            "email": "macaverde@gmail.com"
        }
    ]

    return data_base

def data_community():
    data_base = [
        {
            "name": "amantes do espaco",
            "description": "nos amamos o espaco",
            "admin": "jose_l"
        },
        {
            "name": "gatos fofinhos",
            "description": "veja os gatos mais fofinhos desse app",
            "admin": "lua roxa00"
        },
        {
            "name": "carros esportivos",
            "description": "se voce e amante de carro vai amar essa pagina",
            "admin": "maria_l"
        },
        {
            "name": "mundo oculto",
            "description": "venha para um mundo cheio de misterios",
            "admin": "leonardo2004"
        },
        {
            "name": "Subaqua",
            "description": "embarque nessa jornada e descubra segredos das profundezas dos oceanos",
            "admin": "mat"
        },
        {
            "name": "flor do campo",
            "description": "dicas e muito mais para você cuidar do seu agronegocio",
            "admin": "maca verde00"
        }
    ]

    return data_base

def data_user_whit_community():
    data_base = [
        {
            "name": "jose",
            "password": "Mm@1234",
            "username": "jose_l",
            "email": "jose@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "amantes do espaco"}]
        },
        {
            "name": "maria",
            "password": "Mm@1234",
            "username": "maria_l",
            "email": "maria@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "carros esportivos"}]
        },
        {
            "name": "leo",
            "password": "@leo14M",
            "username": "leonardo2004",
            "email": "leozin@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "mundo oculto"}]
        },
        {
            "name": "matheus",
            "password": "@Arcanjos00",
            "username": "mat",
            "email": "mat@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "Subaqua"}]
        },
        {
            "name": "lua roxa",
            "password": "Pacoca@14",
            "username": "lua roxa00",
            "email": "luaRoxa@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "gatos fofinhos"}]
        },
        {
            "name": "maca verde",
            "password": "macaVerde045@",
            "username": "maca verde00",
            "email": "macaverde@gmail.com",
            "followers": [],
            "following": [],
            "community": [{"name": "flor do campo"}]
        }
    ]

    return data_base

def data_community_whit_user():
    data_base = [
        {
            "name": "amantes do espaco",
            "description": "nos amamos o espaco",
            "member": [{"username": "jose_l", "access": 0}],
            "banned": []
        },
        {
            "name": "gatos fofinhos",
            "description": "veja os gatos mais fofinhos desse app",
            "member": [{"username": "lua roxa00", "access": 0}],
            "banned": []
        },
        {
            "name": "carros esportivos",
            "description": "se voce e amante de carro vai amar essa pagina",
            "member": [{"username": "maria_l", "access": 0}],
            "banned": []
        },
        {
            "name": "mundo oculto",
            "description": "venha para um mundo cheio de misterios",
            "member": [{"username": "leonardo2004", "access": 0}],
            "banned": []
        },
        {
            "name": "Subaqua",
            "description": "embarque nessa jornada e descubra segredos das profundezas dos oceanos",
            "member": [{"username": "mat", "access": 0}],
            "banned": []
        },
        {
            "name": "flor do campo",
            "description": "dicas e muito mais para você cuidar do seu agronegocio",
            "member": [{"username": "maca verde00", "access": 0}],
            "banned": []
        }
    ]
    return data_base
