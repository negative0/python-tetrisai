from Mino import *
from Board import *

from copy import deepcopy
from time import sleep
from os import system
from Quartz import *

import Image
import ImageOps

kpWait = 0.06
lcWait = 0.1

class TetrisBattleController:
	board = None
	curMino = None
	offset = (0, 0)
	expb = None
	player = None
	gameOver = False

	def __init__(self, player):
		self.board = Board()
		self.player = player
		sig = Image.open("sig.png")
		sig = ImageOps.grayscale(sig)
		sigp = sig.load()

		n = []
		for i in range(sig.size[0]):
			n.append(sigp[i, 0])

		# Assinatura em formato de string
		n = ' '.join(map(str, n))

		raw_input("Posicione a janela e pressione enter para comecar...")
		sleep(2)
		scp = self.screenCapture()

		w = scp[1]
		h = scp[2]
		scp = scp[0]


		for j in range(h):
			cl = []
			for i in range(w):
				cl.append(scp[i, j])
			h = ' '.join(map(str, cl))
			m = h.find(n)
			if m >= 0:
				m = len(h[0:m].split(" "))
				print "Signature found on %d, %d" % (m, j)
				#self.offset = (m, j-18)
				self.offset = (m+1, j+4)
				break

	def tick(self):
		self.player.makeMove(self)
	def gameIsOver(self):
		self.gameOver = True

	def screenCapture(self):
		s1 = CGWindowListCreateImage(CGRectInfinite, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowImageDefault)
		s2 = CGImageGetDataProvider(s1)
		s3 = CGDataProviderCopyData(s2)
		w = CGImageGetWidth(s1)
		h = CGImageGetHeight(s1)
		s4 = Image.frombuffer("RGBA", (w, h), s3, 'raw', "BGRA", 0, 1)
		s5 = ImageOps.grayscale(s4)
		s6 = s5.load()

		return (s6, w, h)

	def keyPress(self, keycode):
		keyup = CGEventCreateKeyboardEvent(None, keycode, True)
		keydown = CGEventCreateKeyboardEvent(None, keycode, False)

		CGEventPost(kCGHIDEventTap, keyup)
		sleep(kpWait)
		CGEventPost(kCGHIDEventTap, keydown)
		sleep(kpWait)
		return

	def readScreen(self):
		self.board = Board()
		board = self.readBoard()
		self.curMino = self.readSignature(board)

		mask = ["#"] * 10
		for i in range(19, -1, -1):
			for j in range(10):
				if mask[j] == ".":
					board[i][j] = " "
				if board[i][j] == ".":
					board[i][j] = " "
					mask[j] = "."

		self.board.board = deepcopy(board)

	def readBoard(self):
		board = []
		scp = self.screenCapture()[0]
		
		for j in range(20):
			cl = []
			for i in range(10):
				pxl = (18 * i, 18 * j)
				pxl = (pxl[0] + self.offset[0], pxl[1] + self.offset[1])
				pxl = scp[pxl[0], pxl[1]]

				if pxl > 120:
					cl.append("#")
				elif pxl == 102:
					cl.append(".")
				else:
					cl.append(" ")
			board.append(cl)

		return board

	def readSignature(self, board):
		pid = deepcopy(board)
		for i in range(20):
			for j in range(10):
				if pid[i][j] == '#':
					pid[i][j] = ' '
		pl = []

		for j in pid:
			if '.' in j:
				pl.append(j)

		pid = []
		for l in zip(*pl):
			if '.' in list(l):
				pid.append(l)

		pShape = map(list, zip(*pid))
		pSig = ""
		for line in pShape:
			pSig += ''.join(line)
			pSig += "|"

		pMino = -1
		if pSig == "":
			return -1

		if   pSig == "  .|...|":
			pMino = Tetrominoes.SL
		elif pSig == ".  |...|":
			pMino = Tetrominoes.IL
		elif pSig == " . |...|":
			pMino = Tetrominoes.ST
		elif pSig == "..|..|":
			pMino = Tetrominoes.SQ
		elif pSig == "....|":
			pMino = Tetrominoes.SI
		elif pSig == " ..|.. |":
			pMino = Tetrominoes.SS
		elif pSig == ".. | ..|":
			pMino = Tetrominoes.IS
		else:
			print "pSig desconhecido: %s" % pSig
			return -1

		return pMino


	def getMino(self):
		self.readScreen()
		return Mino(self.curMino)

	def getBoard(self):
		self.readScreen()
		return Board(self.board)

	def makeMove(self, move):
		print move
		b = Board(self.board)
		m = Mino(self.curMino)

		for i in range(move[1]):
			m.rotate()

		m.draw()
		b = b.placeMino(m, move[0])
		b.clearAndReturnLines()
		self.expb = b

		for i in range(move[1]):
			self.keyPress(126)

		pd = (move[0] - 3)
		if pd > 0:
			for i in range(pd):
				self.keyPress(124)
		else:
			for i in range(abs(pd)):
				self.keyPress(123)

		self.keyPress(49)
		sleep(lcWait)
		self.readScreen()


		for i in range(20):
			for j in range(10):
				if self.expb.board[i][j] != self.board.board[i][j]:
					print "Ops!"
					self.expb.draw()
					self.board.draw()
					print "---"
					break


	def draw(self):
		self.board.draw()