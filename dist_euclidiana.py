import math
def dist_euclidiana(v1, v2):
	dim, soma = len(v1), 0
	for i in range(dim):
		soma += math.pow(v1[i] - v2[i], 2)
	return math.sqrt(soma)

# distância euclidiana com numpy
import numpy as np
def dist_euclidiana_np(v1, v2):
	v1, v2 = np.array(v1), np.array(v2)
	diff = v1 - v2
	quad_dist = np.dot(diff, diff)
	return math.sqrt(quad_dist)
