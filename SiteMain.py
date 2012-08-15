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

params = [[1.0001442812185086, 0.927054530945572], [-0.06520063463695669, 1.6071148467167593], [-0.5721303460649061, 0.7555462997056379], [-1.2120473133081755, 1.1268862061682619], [-1.0985186173411812, 0.1580366585795763], [0.10150830180736792, 1.306438603140927]]

p1 = Player(params)
c = TetrisBattleController(p1)

while True:
	c.tick()