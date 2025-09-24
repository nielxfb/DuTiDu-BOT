import json

class FileLoader:
    def load_data(self):
        try:
            with open(self.filepath, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            self.data = {}

    def __init__(self):
        self.filepath = 'datas/schedule.json'
        self.data = None
        self.load_data()