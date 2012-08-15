from Mino import *
from Board import *
from BoardScorer import *

from copy import deepcopy

class Player:
	scorer = None


	def __init__(self, params):
		self.scorer = BoardScorer(params)

	def makeMove(self, controller):
		board = controller.getBoard()
		mino = controller.getMino()

		nextBoards = []

		for c in range(-3, 10):
			for r in range(0, 4):
				nB = board.placeMino(mino, c)

				mino.rotate()

				if nB:
					nB.linesCleared = nB.clearAndReturnLines()
					nB.streak = 0 if nB.linesCleared == 0 else nB.streak + nB.linesCleared
					nextBoards.append( (c, r, nB) )

		if len(nextBoards) == 0:
			controller.gameIsOver()
			return

		scoredBoards = []
		for board in nextBoards:
			scoredBoards.append( ( self.scorer.scoreBoard( board[2] ), board ) )

		scoredBoards.sort(key=lambda row: row[0], reverse=True)

		# Formato (coluna, rotacao)
		move = ( scoredBoards[0][1][0], scoredBoards[0][1][1] )
		controller.makeMove(move)