from . import file_explorer


class ConsoleInput(file_explorer.FileExplorer):
    def __init__(self):
        super().__init__()

    def data_input(self, raw_data):

        data = [x.strip() for x in raw_data]

        for i, key in enumerate(self.parameters.keys()):

            if i >= len(data):
                break

            if key == "K" or key == "M" or key == "N" or key == "T_stop":
                self.parameters[key] = int(data[i])
            elif key == "bool" or key == "record":
                self.parameters[key] = bool(data[i])
            elif key == "W_type" or key == "Sigma" or key == "Mutator":
                self.parameters[key] = data[i]
            else:
                self.parameters[key] = float(data[i])

        self.file_output(self.parameters)