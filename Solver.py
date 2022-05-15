import numpy as np
import math as m

from Generator import Generator as Gen
import Observer as Obs


# Model class in MVP pattern, implementing the SSWM algorithm
class SSWM(Obs.Publisher):
    def __init__(self, K, M, N, subscriber: Obs.Observer,
                 boolean=True, W_type="C", sigma_func="identity",
                 mutator="flipper", T_stop=2_000,
                 beta_parameter=0.99, c_parameter=2,
                 lambda_parameter=2, h=1, p_mut=0.5, record=True):

        # call to parent class init, to ensure publisher-subscriber relation between SSWM and Presenter
        super().__init__(subscriber)

        # helper-class to generate matrices and vectors
        self.generator = Gen(K, M, N, boolean, W_type, sigma_func)

        self.h = h
        self.T_stop = T_stop  # maximum number of steps the algorithm can perform
        self.p_mut = p_mut  # mutation probability

        # generating matrices and vector needed to start calculation
        self.W = self.generator.W_matrix()
        self.B = self.generator.B_matrix()
        self.C = self.generator.C_vector()

        # used to calculate proportion of "max_fitness", which "fitness" value must not cross
        self.beta = beta_parameter

        # C parameter must be larger than 1
        if c_parameter <= 1:
            self.C_parameter = 2
        else:
            self.C_parameter = c_parameter

        # lambda parameter must be larger than 0
        if lambda_parameter <= 0:
            self.Lambda = 2
        else:
            self.Lambda = lambda_parameter

        # selecting the mutate function for fitness vector
        self.mutators = ["flipper"]
        if mutator in self.mutators:
            if mutator == self.mutators[0]:
                self.mutate = self.flipper

        self.max_fitness = self.get_F_max()
        self.fittest = None

        # determines if the algorithm will keep record of generations and their fitnesses
        self.recording = record

        if self.recording:
            # arrays needed to build a plot after algorithm finishes work
            self.generations = []
            self.fitnesses = []

    def get_W(self, fitness_vector):
        return np.dot((self.B @ fitness_vector.T), fitness_vector) * 0.5 + np.dot(self.C, fitness_vector)

    def fitness(self, fitness_vector):
        return self.C_parameter * m.exp(self.Lambda * self.get_W(fitness_vector))

    def get_F_max(self):
        # calculating max_fitness
        inv_B_m = np.linalg.inv(self.B)
        W_max = -0.5 * np.dot(inv_B_m @ self.C.T, self.C)
        return self.C_parameter * m.exp(W_max)

    def flipper(self, genotype):
        # basic mutator - coinflip
        for i in range(len(genotype)):
            if np.random.binomial(1, self.p_mut):
                genotype[i] = 1 - genotype[i]
        return genotype

    def solver(self):
        step = 0
        # generating the initial genotype
        self.genotype = self.generator.S_vector()
        # calculating it's fitness
        fitness_vector = self.generator.F_vector(self.genotype, self.W)
        gen_fitness = self.fitness(fitness_vector)

        self.notify(f"Start_fitness: {gen_fitness}, Max_fitness: {self.max_fitness * self.beta}")

        while step < self.T_stop and gen_fitness < self.max_fitness * self.beta:

            fitness_vector = self.generator.F_vector(self.genotype, self.W)
            gen_fitness = self.fitness(fitness_vector)

            # mutating the genotype
            next_gen = self.mutate(self.genotype.copy())
            # calculating new genotype's fitness
            NG_fitness_vector = self.generator.F_vector(next_gen, self.W)
            next_gen_fitness = self.fitness(NG_fitness_vector)

            # if next_gen fitness is greater than fitness of current generation - the fittest survives
            delta_F = next_gen_fitness - gen_fitness
            if delta_F > 0:
                self.genotype = next_gen

            if self.recording:
                self.notify(f"Generation: {step}, Fitness: {gen_fitness}, "
                            f"diff: {abs(delta_F)}, Gens:{self.genotype}/{next_gen}")
                self.generations.append(step)
                self.fitnesses.append(gen_fitness)
            step += 1

        self.fittest = self.genotype
