import numpy as np

class SSWM:
	'''
	SSWM implementation
	genes - length of genotype [boolean vector]
	fitness - (fitness function, the theoretically possible maximal value of it)
	mutate - mutation function
	"flipper - flips each gene with 50% chance for each"
	T_stop - last generation limit [int]
	beta - critical level of adaptation [0.0, 1.0]
	'''
	def __init__(self, genes=5, fitness=(None,None), mutate="flipper", \
			T_stop=100, beta=0.95):

		self.genotype = np.random.randint(2, size=genes)
		self.T_stop = T_stop
		self.beta = beta
		self.fittest = None
		if fitness != (None, None):
			self.fitness, self.F_max = fitness
		else:
			self.F_max = len(self.genotype)

		if mutate == "flipper":
			self.mutate = self.flipper

	def fitness(self, genotype):
		return sum(genotype)

	def flipper(self, genotype):
		for i in range(len(genotype)):
			if np.random.randint(2, size=1)[0]:
				genotype[i] = 1 - genotype[i]
		return genotype

	def solver(self, silent=False):
		T = 0
		gen_fitness = self.fitness(self.genotype)

		while T < self.T_stop and gen_fitness < self.F_max*self.beta:
			next_gen = self.mutate(self.genotype.copy())
			gen_fitness = self.fitness(self.genotype)
			next_gen_fitness = self.fitness(next_gen)
			F = next_gen_fitness - gen_fitness
			if F > 0:
				self.genotype = next_gen
			
			if not silent:
				print(f"Generation: {T}, Fitness: {gen_fitness}")
			T += 1
		self.fittest = self.genotype

if __name__ == "__main__":
	sswm = SSWM()
	sswm.solver()
	print("\n", sswm.fittest)