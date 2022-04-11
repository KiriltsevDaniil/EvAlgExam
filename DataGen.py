import numpy as np

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
	pass

def W_matrix_gen(variant='C', K=4, M=10):
	assert M > 1, "Matrix should be bigger than 1x1"
	assert K >= 0, "parameter K should be higher than -1"
	assert K <= M, "parameter K can not be higher than M"
	if variant == 'C':
		W_matrix = W_var_C_gen(K, M)
	elif variant == 'D':
		W_matrix = W_var_D_gen(K, M)
	else:
		raise Exception("Variant has to be either C or D")
	return W_matrix

if __name__ == '__main__':
	matrix = W_matrix_gen()
	print(matrix)