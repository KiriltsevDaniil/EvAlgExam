import numpy as np
import math as m
import DataGen as dg

class SSWM:
	'''Using SSWM in case of our problem'''
	def __init__(self, W_matrix, B_matrix, C_vector, mutate="flipper", \
		T_stop=2_000, beta=0.99, C_parm=2, lambda_parm=2, N=3,h=1, p_mut=0.5):
		
		assert C_parm > 1, "C_parm has to be more than 1"
		assert lambda_parm > 0, "lambda_parm has to be more than 0"


		self.N = N
		self.h = h
		self.T_stop = T_stop
		self.p_mut = p_mut

		self.W_m = W_matrix
		self.B_m = B_matrix
		self.C_v = C_vector

		self.C_parm = C_parm
		self.lambda_parm = lambda_parm
		self.beta = beta

		if mutate == "flipper":
			self.mutate = self.flipper

		self.F_max = self.get_F_max()
		self.fittest = None

		self.generations = []
		self.fitnesses = []

	def W(self, f_v):
		return np.dot((self.B_m @ f_v.T),f_v)*0.5 + np.dot(self.C_v, f_v)

	def fitness(self, f_v):
		return self.C_parm * m.exp(self.lambda_parm * self.W(f_v))

	def get_F_max(self):
		inv_B_m = np.linalg.inv(self.B_m)
		W_max = -0.5 * np.dot(inv_B_m @ self.C_v.T,self.C_v)
		return self.C_parm * m.exp(W_max)

	def flipper(self, genotype):
		for i in range(len(genotype)):
			if np.random.binomial(1, self.p_mut):
				genotype[i] = 1 - genotype[i]
		return genotype

	def solver(self, silent=False):
		T = 0
		self.S_v = dg.S_vector_gen(N=self.N)
		f_v_gen = dg.F_vector_gen(self.S_v, self.W_m)
		gen_fitness = self.fitness(f_v_gen)
		print(f"Start_fitness: {gen_fitness}", f"Max_fitness: {self.F_max*self.beta}")
		while T < self.T_stop and gen_fitness < self.F_max*self.beta:
			
			f_v_gen = dg.F_vector_gen(self.S_v, self.W_m)
			gen_fitness = self.fitness(f_v_gen)

			next_gen = self.mutate(self.S_v.copy())
			f_v_next_gen = dg.F_vector_gen(next_gen, self.W_m)
			next_gen_fitness = self.fitness(f_v_next_gen)

			F = next_gen_fitness - gen_fitness
			if F > 0:
				self.S_v = next_gen
			
			if not silent:
				print(f"Generation: {T}, Fitness: {gen_fitness}, diff: {F}, Gens:{self.S_v}/{next_gen}")
				self.generations.append(T)
				self.fitnesses.append(gen_fitness)
			T += 1
		self.fittest = self.S_v


if __name__ == "__main__":
	pass