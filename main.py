import Solver as slvr
import numpy as np

from View import View

r_seed = np.random.randint(10000)
np.random.seed(r_seed)


K=2
M=5
N=5

sswm = slvr.SSWM(K, M, N)
sswm.solver()
print("\n", sswm.fittest)

plot = View(sswm.F_max, sswm.generations, sswm.fitnesses, r_seed)
plot.show()