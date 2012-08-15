from Mino import *
from Board import *
from DummyController import *

from copy import deepcopy
from random import choice

class DuelController:
	p1_controller = None
	p2_controller = None
	p1_linesCleared = None
	p2_linesCleared = None
	p1_linesSent = None
	p2_linesSent = None
	p1_victory = None
	p2_victory = None

	p1_score = None
	p2_score = None

	gameOver = None

	def __init__(self, p1, p2):
		self.p1_controller = DummyController(p1)
		self.p2_controller = DummyController(p2)
		self.p1_linesCleared = 0
		self.p2_linesCleared = 0
		self.p1_linesSent = 0
		self.p2_linesSent = 0
		self.p1_victory = 0
		self.p2_victory = 0
		self.p1_score = 0
		self.p2_score = 0
		self.gameOver = False

	def tick(self):
		turnMino = choice(Tetrominoes.minoes)
		self.p1_controller.curMino = turnMino
		self.p2_controller.curMino = turnMino

		self.p1_controller.tick()
		self.p2_controller.tick()

		p1_sentLines = self.linesToSend(self.p1_controller.streak, self.p1_controller.linesCleared - self.p1_linesCleared)
		self.p1_linesCleared = self.p1_controller.linesCleared
		self.p2_controller.addLines(p1_sentLines)
		self.p1_linesSent += p1_sentLines

		p2_sentLines = self.linesToSend(self.p2_controller.streak, self.p2_controller.linesCleared - self.p2_linesCleared)
		self.p2_linesCleared = self.p2_controller.linesCleared
		self.p1_controller.addLines(p2_sentLines)
		self.p2_linesSent += p2_sentLines

		if self.p1_controller.gameOver:
			self.p2_victory = 1
			self.gameOver = True
			self.setScores()
		elif self.p2_controller.gameOver:
			self.p1_victory = 1
			self.gameOver = True
			self.setScores()

	def setScores(self):
		self.p1_score = 6 * self.p1_victory + 2 * self.p1_linesSent + self.p1_linesCleared
		self.p2_score = 6 * self.p2_victory + 2 * self.p2_linesSent + self.p2_linesCleared

	def linesToSend(self, streak, clearedLines):
		return clearedLines if streak > clearedLines else 0

	def draw(self):
		print "-" * 23
		for i in range(20):
			print '|%s|%s|' % (''.join(self.p1_controller.board.board[i]), ''.join(self.p2_controller.board.board[i]))
		print "-" * 23