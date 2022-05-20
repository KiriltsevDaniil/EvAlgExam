import CLI as cli
import Presenter

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sys import argv



def experiment_params(alpha, K=7, N=10, h=0, C=2, beta=2):
    k = 0.75
    K= int(alpha*N * k)
    parameters = {
            "K": K,
            "M": alpha*N,
            "N": N,
            "bool": 1,
            "W_type": "C",
            "Sigma": "identity",
            "Mutator": "flipper",
            "T_stop": 2000,
            "b": beta,
            "c": C,
            "lambda": 1,
            "h": h,
            "p_mut": 0.5,
            "record": 0
            }
    return parameters

def Plotter(x, y, z):
	fig = plt.figure()
	ax = Axes3D(fig)
	surf = ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.1)
	fig.colorbar(surf, shrink=0.5, aspect=5)
	plt.savefig('teste.pdf')
	plt.show()

def experiment(alpha=1, step=6, alpha_max=20, N_mc=5):
	global_res, alphas, Ks = [], [], []
	while alpha <= alpha_max:
		print(alpha)
		parameters = experiment_params(alpha)
		Ks.append(parameters["K"])
		local_res = []
		for i in range(N_mc):
			model = Presenter.Presenter(True, parameters)
			result = model.run_algorithm(very_noisy=False)
			local_res.append(result)
		global_res.append(sum(local_res)/N_mc)
		alphas.append(alpha)
		alpha += step
	Plotter(global_res, alphas, Ks)
	#So after a couple of thousands rolls we have array of mean


if __name__ == '__main__':
	experiment()