import json

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
