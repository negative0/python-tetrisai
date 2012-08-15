from random import randint, uniform
from copy import deepcopy

def mutate(params):
	geneIndex = randint(0, len(params) - 1)
	mutationType = randint(0, 1)

	newParams = deepcopy(params)

	if mutationType == 0:
		newParams[geneIndex][mutationType] *= uniform(-2.0, 2.0)
	else:
		newParams[geneIndex][mutationType] *= uniform(0.9, 1.1)

	return newParams

def crossover(p1, p2):
	newParams = []

	for i in range( len(p1) ):
		if randint(0, 1) == 0:
			newParams.append(p1[i])
		else:
			newParams.append(p2[i])

	return newParams

def randomparams(numbases):
	newParams = []
	for i in range(numbases):
		newParams.append([uniform(-2.0, 2.0), uniform(0.0, 2.0)])

	return newParams