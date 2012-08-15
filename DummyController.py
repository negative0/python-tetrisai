from Mino import *
from Board import *

from copy import deepcopy
from random import choice

class DummyController:
	board = None
	curMino = None
	linesCleared = None
	gameOver = None
	player = None
	streak = None

	def __init__(self, player):
		self.board = Board()
		self.curMino = choice(Tetrominoes.minoes)
		self.linesCleared = 0
		self.streak = 0
		self.player = player
		gameOver = False

	def tick(self):
		self.player.makeMove(self)

	def getMino(self):
		return Mino(self.curMino)

	def getBoard(self):
		return Board(self.board)

	def makeMove(self, move):
		mino = Mino(self.curMino)
		for i in range(move[1]):
			mino.rotate()

		newBoard = self.board.placeMino(mino, move[0])
		if newBoard:
			self.board = newBoard
		else:
			print "Controller: invalid move received"
			raise

		clearedLines = self.board.clearAndReturnLines()
		
		if clearedLines == 0:
			self.streak = 0
		else:
			self.streak += clearedLines

		self.linesCleared += clearedLines
		self.curMino = choice(Tetrominoes.minoes)

	def gameIsOver(self):
		self.gameOver = True

	def addLines(self, num):
		self.board.addLines(num)

	def draw(self):
		self.board.draw()