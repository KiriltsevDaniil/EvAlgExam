import numpy as np
import math


class Generator:
    def __init__(self, K, M, N, boolean, W_type, sigma):

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

        # determines if B_matrix and C_vector will be filled with boolean of float values
        self.boolean = boolean

        self.sigma_options = ["identity", "fermi"]
        # determining the sigma function used to generate fitness vector
        if sigma in self.sigma_options:
            self.sigma = sigma
        else:
            self.sigma = self.sigma_options[0]

        self.W_matrix_types = ['C', 'D']
        # determining the type of W matrix generated
        if W_type in self.W_matrix_types:
            self.W_matrix_type = W_type
        else:
            self.W_matrix_type = self.W_matrix_types[0]

    def S_vector(self):
        return np.random.randint(2, size=self.N)

    def W_type(self):
        return True if self.W_matrix_type == self.W_matrix_types[0] else False

    def W_matrix(self):
        cases = [-1, 1]
        i = 0
        w_matrix = np.random.randint(1, size=(self.M, self.M))

        if self.W_type():
            # Generating C type matrix
            for row in w_matrix:
                row[np.random.choice(len(row), size=self.K, replace=False)] = 1
                w_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
                i += 1
        else:
            # Generating D type matrix
            k = np.random.poisson(lam=self.K, size=10)
            for row in w_matrix:
                row[np.random.choice(len(row), size=k[i], replace=False)] = 1
                w_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
                i += 1

        return w_matrix

    def C_vector(self):
        if self.boolean:
            return np.random.rand(self.M)
        else:
            return np.random.randint(2, size=self.M)

    def B_matrix(self):
        if self.boolean:
            B_matrix = np.random.rand(self.M, self.M)
        else:
            B_matrix = np.random.randint(2, size=(self.M, self.M))

        return np.tril(B_matrix) + np.tril(B_matrix, -1).T

    def sigma_func(self):
        # function to determine sigma_function needed in calculation of F_vector
        if self.sigma == self.sigma_options[0]:
            return lambda z: z
        else:
            return lambda z, a=0.5: pow((1 + math.exp(-a * z)), -1)

    def F_vector(self, genotype, W_matrix, h=0):
        # calculation of fitness vector
        sigma = self.sigma_func()
        genotype = np.resize(genotype, (1, len(W_matrix[0])))
        f_vector = []

        for row in W_matrix:
            f_vector.append(sigma((row * genotype).sum() - h))

        return np.asarray(f_vector)
