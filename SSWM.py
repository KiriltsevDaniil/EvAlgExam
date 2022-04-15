import numpy as np
import matplotlib.pyplot as plt
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
	def __init__(self, genotype=None, fitness=(None,None), mutate="flipper", \
			T_stop=5000, beta=0.95):
		
		if type(genotype) == type(None):
			self.genotype = np.random.randint(2, size=30)
		else:
			self.genotype = genotype
		
		self.T_stop = T_stop
		self.beta = beta

		self.generations = []
		self.fitnesses = []
		
		if fitness != (None, None):
			self.fitness, self.F_max = fitness
		else:
			self.F_max = len(self.genotype)
			self.fitness = self.test_fitness

		if mutate == "flipper":
			self.mutate = self.flipper

		self.fittest = None

	def plotter(self):
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		plt.axhline(y=self.F_max, color='r', label='Max Fitness')
		plt.plot(self.generations, self.fitnesses, 'b', label='Fitness')
		plt.grid()
		plt.xlabel("Generation T")
		plt.ylabel("Fitness F")
		plt.legend(loc='upper left')
		plt.show()

	def test_fitness(self, genotype):
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
			self.generations.append(T)
			self.fitnesses.append(gen_fitness)
			T += 1
		self.fittest = self.genotype

if __name__ == "__main__":
	sswm = SSWM()
	sswm.solver()
	sswm.plotter()
	print("\n", sswm.fittest)