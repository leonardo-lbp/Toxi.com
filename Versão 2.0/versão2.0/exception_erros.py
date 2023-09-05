#classe de erro para senha invalida
class InvalidPasswordError(ValueError):
    def __init__(self, message="A senha é inválida."):
        super().__init__(message)

#classe de erro para username invalido
class InvalidUsernameError(ValueError):
    def __init__(self, message="O Usuario já existe"):
        super().__init__(message)

#classe de erro para email invalido
class InvalidEmailError(ValueError):
    def __init__(self, message="O email digitado é inválido"):
        super().__init__(message)

#classe de erro para nome de usuario não inserido
class InvalidUserNameError(ValueError):
    def __init__(self, message="Nome não inserido"):
        super().__init__(message)

#classe de erro para name de comunidade invalido
class InvalidCommunityNameError(ValueError):
    def __init__(self, message="O nome da comunidade já existe"):
        super().__init__(message)

#classe de erro para user não encontrado
class InvalidUserError(NameError):
    def __init__(self, message="O usuario não foi encontrado"):
        super().__init__(message)

#classe de erro para comunidae não encontrada
class InvalidCommunityError(NameError):
    def __init__(self, message="A comunidade não foi encontrado"):
        super().__init__(message)

#classe de erro para o nível de acesso
class InvalidAccessUserError(NameError):
    def __init__(self, message="Você não possuí acesso"):
        super().__init__(message)

#classe do erro de login
class InvaldLoginError(NameError):
    def __init__(self, message="Username ou senha inválidos"):
        super().__init__(message)

#classe do erro de username
class InvalidUsernameError2(ValueError):
    def __init__(self, message="Username não preenchido"):
        super().__init__(message)

#classe de erro de dados
class InvalidDataError(NameError):
    def __init__(self, message="Dados não encontrados"):
        super().__init__(message)
