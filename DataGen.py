import numpy as np
import math as m

sigma_option = ["fermi", "identity"]
W_types = ['C', 'D']

def S_vector_gen(N=10):
	return np.random.randint(2, size=N)

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
	assert opt in W_types, "Matrix has to be either C or D type"
	if opt == 'C':
		W_matrix = W_var_C_gen(K, M)
	elif opt == 'D':
		W_matrix = W_var_D_gen(K, M)
	return W_matrix

def sigma_f(opt="fermi"):
	if opt == 'fermi':
		f_sigma = lambda z, a=0.5: pow((1 + m.exp(-a*z)), -1)
	elif opt == 'identity':
		f_sigma = lambda z: z
	return f_sigma

def C_vector_gen(M=10):#Right now it's boolean
	#return np.random.randint(2, size=M)
	return np.random.rand(M)

def F_vector_gen(genotype, W_matrix, h=0, sigma_opt="identity"):
	assert sigma_opt in sigma_option, \
	f"Choose one of the existing sigma functions: {sigma_option}"
	sigma = sigma_f(sigma_opt)
	f_v = []
	genotype = np.resize(genotype, (1, len(W_matrix[0])))
	for row in W_matrix:
		f_v.append(sigma((row*genotype).sum() - h))
	return np.asarray(f_v)


def B_matrix_gen(M=10): #Right now it's boolean
    #B_matrix = np.random.randint(2,size=(M,M))
    B_matrix = np.random.rand(M,M)
    return np.tril(B_matrix) + np.tril(B_matrix, -1).T

if __name__ == '__main__':
	pass