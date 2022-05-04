import numpy as np
import math


class Generator:
    def __init__(self, K, M, N):

        if M <= 1 or K < 0 or K > M:
            # checking if parameters satisfy W_matrix generation restrictions
            # if the don't - replace them with the standard 2-5-5
            self.K = 2
            self.M = 5
            self.N = 5

            print("conditions for correct generations aren't met!")
            print(f"Changed values: K = {self.K}, M = {self.M}, N = {self.N}\n")
        else:
            self.K = K
            self.M = M
            self.N = N

        self.sigma_options = ["fermi", "identity"]
        self.W_types = ['C', 'D']

    def S_vector(self):
        return np.random.randint(2, size=self.N)

    def check_W_type(self, type):
        # helper function to check if the required W_matrix type can be provided by Generator
        if type in self.W_types:
            if type == self.W_types[0] or type == self.W_types[1]:
                return True

        return False

    def W_generator(self, d_type=False):
        cases = [-1, 1]
        i = 0
        W_matrix = np.random.randint(1, size=(self.M, self.M))

        if not d_type:
            # Generating C type matrix
            for row in W_matrix:
                row[np.random.choice(len(row), size=self.K, replace=False)] = 1
                W_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
                i += 1
        else:
            # Generating D type matrix
            k = np.random.poisson(lam=self.K, size=10)
            for row in W_matrix:
                row[np.random.choice(len(row), size=k[i], replace=False)] = 1
                W_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
                i += 1

        return W_matrix

    def W_matrix(self, option="C"):
        if self.check_W_type(option):
            return self.W_generator(True if option == self.W_types[1] else False)
        else:
            print("Matrix has to be either C or D type")

    def C_vector(self, boolean=True):
        if boolean:
            # boolean vector
            return np.random.randint(2, size=self.M)
        else:
            # float vector
            return np.random.rand(self.M)

    def B_matrix(self, boolean=True):
        if boolean:
            # boolean matrix
            B_matrix = np.random.randint(2, size=(self.M, self.M))
        else:
            # float matrix
            B_matrix = np.random.rand(self.M, self.M)

        return np.tril(B_matrix) + np.tril(B_matrix, -1).T

    def sigma_func(self, sigma):
        # function to determine sigma_function needed in calculation of F_vector
        if sigma == self.sigma_options[1]:
            return lambda z: z
        else:
            return lambda z, a=0.5: pow((1 + math.exp(-a * z)), -1)

    def F_vector(self, genotype, W_matrix, h=0, sigma="identity"):
        # calculation of fitness vector
        if sigma in self.sigma_options:
            sigma_f = self.sigma_func(sigma)
            genotype = np.resize(genotype, (1, len(W_matrix[0])))
            f_vector = []

            for row in W_matrix:
                f_vector.append(sigma_f((row * genotype).sum() - h))

            return np.asarray(f_vector)
        else:
            print(f"Choose one of the existing sigma functions: {self.sigma_options}")
