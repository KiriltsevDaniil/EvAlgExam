import Solver as slvr
# import DataGen as dg
import numpy as np

from View import View
from Generator import Generator

# r_seed = np.random.randint(10000)
# np.random.seed(r_seed)
r_seed = 4783


K=2
M=5
N=5

sswm = slvr.SSWM(K=K, M=M, N=N)
sswm.solver()
print("\n", sswm.fittest)

vw = View(sswm.F_max, sswm.generations, sswm.fitnesses, r_seed)
vw.show()
