import json
from account import Account
from community import Community

class Data:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
        
    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


class userdata(Data):
    def __init__(self, filename="Conta.json"):
        super().__init__(filename)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                print("Dados de usuarios carregados com sucesso!")
                return data
        except FileNotFoundError:
            return []
        
    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


class communiytdata(Data):
    def __init__(self,filename="Comunidade.json"):
        super().__init__(filename)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                print("Dados de comunidades carregados com sucesso!")
                return data
        except FileNotFoundError:
            return []
        
    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
