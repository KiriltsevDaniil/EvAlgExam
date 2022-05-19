import json


class FileExplorer:
    def __init__(self):
        self.path = "./data/config.json"
        self.file = None

        self.parameters = {
            "K": 3,
            "M": 5,
            "N": 5,
            "bool": 1,
            "W_type": "C",
            "Sigma": "identity",
            "Mutator": "flipper",
            "T_stop": 2000,
            "b": 2,
            "c": 2,
            "lambda": 1,
            "h": 1,
            "p_mut": 0.5,
            "record": 1
        }

        # self.open_file()
        self.file = open(self.path, "w+")
        json.dump(self.parameters, self.file, indent="\t")

    def open_file(self, mode="r"):

        self.close_file()
        try:
            self.file = open(self.path, mode)
        except FileNotFoundError:
            self.file = open(self.path, "w+")
            json.dump(self.parameters, self.file, indent="\t")

        if self.file.closed:
            print(f"Couldn't open file at {self.path}")

    def close_file(self):
        if self.file:
            self.file.close()

    def file_input(self):
        if not self.file.closed:
            self.parameters = json.load(self.file)
        else:
            print(f"Couldn't read file at {self.path}")

    def file_output(self, data : dict):
        self.close_file()
        self.open_file("w+")
        if not self.file.closed:
            json.dump(data, self.file, indent="\t")
        else:
            print(f"Couldn't write to file at {self.path}")


