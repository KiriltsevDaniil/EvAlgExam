import numpy as np
import math as m

sigma_option = ["fermi", "identity"]

def W_var_C_gen(K, M):
	cases = [-1, 1]
	i = 0
	W_matrix = np.random.randint(1, size=(M, M))
	for row in W_matrix:
		row[np.random.choice(len(row), size=K, replace=False)] = 1
		W_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
		i += 1
	return W_matrix

def W_var_D_gen(K, M):
	cases = [-1, 1]
	i = 0
	k = np.random.poisson(lam=K, size=10)
	W_matrix = np.random.randint(1, size=(M, M))
	for row in W_matrix:
		row[np.random.choice(len(row), size=k[i], replace=False)] = 1
		W_matrix[i] = [cases[np.random.binomial(1, .5)] if x == 1 else x for x in row]
		i += 1
	return W_matrix

def W_matrix_gen(opt='C', K=4, M=10):
	assert M > 1, "Matrix should be bigger than 1x1"
	assert K >= 0, "parameter K should be higher than -1"
	assert K <= M, "parameter K can not be higher than M"
	if opt == 'C':
		W_matrix = W_var_C_gen(K, M)
	elif opt == 'D':
		W_matrix = W_var_D_gen(K, M)
	else:
		raise Exception("Matrix has to be either C or D type")
	return W_matrix

def sigma_f(opt="fermi"):
	if opt == 'fermi':
		f_sigma = lambda z, a=0.5: pow((1 + m.exp(-a*z)), -1)
	elif opt == 'identity':
		f_sigma = lambda z: z
	return f_sigma

def C_vector_gen(M=10):
	return np.random.rand(M)

def f_vector_gen(genotype, W_matrix, h=0.2, sigma_opt="fermi"):
	assert sigma_opt in sigma_option, \
	f"Choose one of the existing sigma functions: {sigma_option}"
	sigma = sigma_f(sigma_opt)
	f = []
	for row in W_matrix:
		summa = 0
		i = 0
		for element in row:
			summa = element + genotype[i]
			i += 1
		f.append(sigma(summa - h))
	return np.asarray(f)


def B_matrix_gen(M=10):
    B_matrix = np.random.rand(M,M)
    return B_matrix + B_matrix.T - np.diag(B_matrix.diagonal())

if __name__ == '__main__':
	pass