import Solver as slvr
import numpy as np
import matplotlib.pyplot as plt

r_seed = np.random.randint(10000)
np.random.seed(r_seed)


K=2
M=5
N=5

sswm = slvr.SSWM(K, M, N)
sswm.solver()
print("\n", sswm.fittest)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.axhline(y=sswm.F_max, color='r', label='Max Fitness')
plt.plot(sswm.generations, sswm.fitnesses, 'b', label='Fitness')
plt.grid()
caption= f"seed: {r_seed}"
plt.xlabel("Generation T")
plt.ylabel("Fitness F")
plt.legend(loc='upper left')
plt.figtext(0.5, 0.01, caption, wrap=True, horizontalalignment='left', fontsize=12)
plt.show()