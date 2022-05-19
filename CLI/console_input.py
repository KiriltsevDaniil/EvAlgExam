from . import file_explorer


class ConsoleInput(file_explorer.FileExplorer):
    def __init__(self):
        super().__init__()

    def data_input(self, raw_data):

        data = [x.strip() for x in raw_data]

        for i, key in enumerate(self.parameters.keys()):

            if i >= len(data):
                break

            self.parameters[key] = data[i]

        self.file_output(self.parameters)