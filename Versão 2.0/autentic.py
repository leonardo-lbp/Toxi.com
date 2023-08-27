import re

#classe para autenticar variaveis
class autentic:
    #checa se já existe uma conta com o mesmo username
    def checkusername(username, checklist):
        for check in checklist:
            if username == check["username"]:
                return 1
        return 0
    
    def checkaccess(username, checklist):
        for check in checklist["member"]:
            if check["username"] == username:
                return check["access"]
        return 3

    #checa se já existe uma comunidade com o mesmo nome
    def checkcommunityname(name, checklist):
        for check in checklist:
            if name == check["name"]:
                return 1
        return 0
    
    #acha os dados do usuário e retorna eles
    def finduser(username, checklist):
        for check in checklist:
            if username == check["username"]:
                return check
        return {}
    
    #acha os dados da comunidade e retorna eles
    def findcommunity(name, checklist):
        for check in checklist:
            if name == check["name"]:
                return check
        return {}

    #checa se a senha é válida
    def checkpassword(password):
        if len(password) < 6:
            return 1
        
        if not re.search(r"[a-z]", password):
            return 1
        
        if not re.search(r"[A-Z]", password):
            return 1
        
        if not re.search(r"\d", password):
            return 1
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return 1

        return 0

    #checa se o email é válido
    def checkemail(email):
        defaut_email = r'^[a-zA-Z0-9._%+=#]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9].+$'
        if not re.match(defaut_email, email):
            return 1
        return 0

    #realiza o login
    def login(username, password, checklist):
        for checkusername in checklist:
            if checkusername['username'] == username and checkusername['password'] == password:
                return 1   
        return 0
