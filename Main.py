from Board import *
from Player import *
from DummyController import *
from TetrisBattleController import *
from DuelController import *

from BoardScorer import *
from Mino import *
from Genetic import *
from random import uniform, sample
from copy import deepcopy

popSize = 10
xoverP = 0.95
mutatP = 0.35

def genPopulation(baseParams = None):
	population = []

	if baseParams == None:

		# Gerar a populacao inicial aleatoriamente
		for i in range(popSize):

			cp = randomparams(6)
			if uniform(0.0, 1.0) < mutatP:
				cp = mutate(cp)

			population.append(cp)

	else:

		# Gerar a partir do melhor conhecido
		for i in range(popSize):

			cp = baseParams
			if uniform(0.0, 1.0) < mutatP:
				cp = mutate(cp)

			population.append(cp)

	return population

def geneticCompare(param1, param2):
	p1 = Player(param1)
	p2 = Player(param2)
	c = DuelController(p1, p2)

	for i in range(120):
		c.tick()
		if c.gameOver:
			break

	c.draw()
	if c.p1_victory == c.p2_victory:
		return c.p1_score - c.p2_score
	else:
		return c.p1_victory - c.p2_victory

def completePopulation(pop):
	population = deepcopy(pop)
	pp = []
	for i in range( len(population) ):
		for j in range( len(population) - i ):
			pp.append(population[i])

	while len(population) < popSize:
		parents = sample(pp, 2)

		if uniform(0, 1) < xoverP:
			offsp = crossover(parents[0], parents[1])
		elif uniform(0, 1) < 0.5:
			offsp = parents[0]
		else:
			offsp = parents[1]

		if uniform(0, 1) < mutatP:
			offsp = mutate(offsp)

		population.append(offsp)

	return population


population = genPopulation([[-1.7117758453328387, 0.927054530945572], [-0.06520063463695669, 1.6071148467167593], [-1.0685820192025854, 0.7555462997056379], [-1.2120473133081755, 1.1268862061682619], [0.7534483110011649, 0.1580366585795763], [0.10150830180736792, 1.306438603140927]])
i = 0
try:
	while True:
		print "Generation %d" % i
		population.sort(cmp=geneticCompare)
		population.reverse()
		population = population[:5]
		population = completePopulation(population)
		print "Best: ",
		print population[0]
		i += 1
except:
	print "Best: ",
	print population[0]
