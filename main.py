import Solver as slvr
import DataGen as dg
import numpy as np

from View import View

r_seed = np.random.randint(10000)
np.random.seed(r_seed)


K=2
M=5
N=5
W_m = dg.W_matrix_gen(K=K, M=M)
B_m = dg.B_matrix_gen(M=M)
C_v = dg.C_vector_gen(M=M)

sswm = slvr.SSWM(W_m, B_m, C_v, N=N)
sswm.solver()
print("\n", sswm.fittest)

vw = View(sswm.F_max, sswm.generations, sswm.fitnesses, r_seed)
vw.show()
