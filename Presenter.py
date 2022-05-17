import numpy as np

from Solver import SSWM
from View import View


# Presenter class of MVP pattern
class Presenter():
    def __init__(self, show_result=True):

        K = 30
        M = 50
        N = 50

        # generating a seed for further random generator usage
        self.seed = np.random.randint(10000)
        np.random.seed(self.seed)

        # establishing Model and View modules
        self.model = SSWM(K, M, N, record=show_result)
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
