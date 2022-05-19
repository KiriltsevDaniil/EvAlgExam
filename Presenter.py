import numpy as np

from Solver import SSWM
from View import View

from CLI import file_input
from CLI import console_input


# Presenter class of MVP pattern
class Presenter():
    def __init__(self):

        # Initializing console and file handlers
        self.file_input = file_input.FileInput()
        self.console_input = console_input.ConsoleInput()

        self.get_data()

        # generating a seed for further random generator usage
        self.seed = np.random.randint(10000)
        np.random.seed(self.seed)

        # establishing Model and View modules
        self.initialize_model()
        self.view = View()

    def run_algorithm(self):
        self.model.solver()
        self.view.fill_chart(self.model.max_fitness,
                             self.model.generations,
                             self.model.fitnesses,
                             self.seed)

        self.get_result()

    def get_result(self):
        self.view.show(self.model.fittest)

    def initialize_model(self):
        parameters = self.file_input.get_from_file()

        self.model = SSWM(
            K=parameters["K"],
            M=parameters["M"],
            N=parameters["N"],
            boolean=parameters["bool"],
            W_type=parameters["W_type"],
            sigma_func=parameters["Sigma"],
            mutator=parameters["Mutator"],
            T_stop=parameters["T_stop"],
            beta_parameter=parameters["b"],
            c_parameter=parameters["c"],
            lambda_parameter=parameters["lambda"],
            h=parameters["h"],
            p_mut=parameters["p_mut"],
            record=parameters["record"]
        )

    def get_data(self):
        raw_data = input().split()

        if raw_data:
            self.console_input.data_input(raw_data)
