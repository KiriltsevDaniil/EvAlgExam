import numpy as np

from View import View
from Solver import SSWM

r_seed = np.random.randint(10000)
np.random.seed(r_seed)


K=2
M=5
N=5

sswm = SSWM(K, M, N)
sswm.solver()
print("\n", sswm.fittest)

plot = View(sswm.max_fitness, sswm.generations, sswm.fitnesses, r_seed)
plot.show()