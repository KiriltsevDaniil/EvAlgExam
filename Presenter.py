import numpy as np

from Solver import SSWM
from View import View
from Observer import Observer


# Presenter class of MVP pattern
class Presenter(Observer):
    def __init__(self, K: int, M: int, N: int, show_result=True):

        # generating a seed for further random generator usage
        self.seed = np.random.randint(10000)
        np.random.seed(self.seed)

        # establishing Model and View modules
        self.model = SSWM(K, M, N, self, record=show_result)
        self.view = View()

        # calling parent init just in case
        super().__init__()

    def run_algorithm(self):
        self.model.solver()
        self.view.fill_chart(self.model.max_fitness,
                             self.model.generations,
                             self.model.fitnesses,
                             self.seed)

        self.get_result()

    def get_result(self):
        self.view.show(self.model.fittest)

    def update(self, message):
        self.view.console_output(message)