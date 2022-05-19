import json


class FileInput():
    def __init__(self):
        self.path = "./data/config.json"
        self.parameters = {
            "K": 0,
            "M": 0,
            "N": 0,
            "bool": 0,
            "W_type": 0,
            "Sigma": 0,
            "Mutator": 0,
            "T_stop": 0,
            "b": 0,
            "c": 0,
            "lambda": 0,
            "h": 0,
            "p_mut": 0,
            "record": 0
        }

    def data_input(self):
        with open(self.path, "r") as file:
            self.parameters = json.load(file)

    def get_data(self):
        return self.parameters


