import SSWM as sswm
import numpy as np
import math as m
import DataGen as dg

def W(B_matrix, C_vector, f_vector):
	return np.dot(np.matmul(B_matrix,f_vector), f_vector)/2 + np.dot(C_vector, f_vector)

def fitness(C_parm, lambda_parm, B_matrix, C_vector):
	return C_parm * m.exp(lambda_parm*W(B_matrix, C_vector, f_vector))

def get_F_max(C_parm):
	W_max = -0.5 * np.dot(np.matmul(np.linalg.inv(B_matrix),C_vector),C_vector)
	return C_parm * m.exp(W_max)

class Solver:
	'''Using SSWM in case of our problem'''
	def __init__(self, C_parm=5, lambda_parm=3, EvAlg=None):
		assert C_parm > 1, "C_parm has to be more than 1"
		assert lambda_parm > 0, "lambda_parm has to be more than 0"

		self.C_parm = C_parm
		self.lambda_parm = lambda_parm
		self.ea = EvAlg

if __name__ == "__main__":
	pass