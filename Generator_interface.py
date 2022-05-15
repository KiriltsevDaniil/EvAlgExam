class IGenerator:
    def __init__(self):

        self.W_matrix_types = ['C', 'D']
        self.sigma_options = ["identity", "fermi"]

    def S_vector(self):
        pass

    def W_matrix(self):
        pass

    def C_vector(self):
        pass

    def B_matrix(self):
        pass

    def F_vector(self, genotype, W_matrix, h=0):
        pass