from . import file_explorer


class FileInput(file_explorer.FileExplorer):
    def __init__(self):
        super().__init__()

    def data_input(self):
        self.open_file()
        self.file_input()
        self.close_file()

    def get_from_file(self):
        self.data_input()
        return self.parameters


