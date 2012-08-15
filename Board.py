from Mino import *
from copy import deepcopy
from random import randint

class Board:
  board = []
  linesCleared = 0
  streak = 0

  def __init__(self, board = False):
    if board:
      self.board = deepcopy(board.board)
    else:
      self.board = []
      for i in range(20):
        cl = []
        for j in range(10):
          cl.append(' ')
        self.board.append(cl)

  # Verifica colisao entre Mino e o board atual
  def checkCollide(self, mino, i0, j0):
    for i in range(len(mino.shape)):
      for j in range(len(mino.shape)):
        boardchar = self.getPos(i0+i, j0+j)
        minochar = mino.shape[i][j]
        if(boardchar == "#" and minochar == "#"):
          return True
    
    return False
  
  # Ignorando o teto como colisao
  def getPos(self, i, j):
    if i < 0: 
      return ' '
    
    return "#" if (j < 0 or j > 9 or i > 19) else self.board[i][j]

  def setPos(self, i, j, v):
    if i < 0 or i > 19 or j < 0 or j > 9:
      return
    
    self.board[i][j] = v

  # Verifica colisao entre Mino e o teto
  def checkCeilCollide(self, mino, i0, j0):
    for i in range(len(mino.shape)):
      for j in range(len(mino.shape)):
        boardchar = "#" if (i0+i < 0) else ' '
        minochar = mino.shape[i][j]
        if(boardchar == "#" and minochar == "#"):
          return True
    
    return False

  # Imprime o estado atual do board no console
  def draw(self):
    print "-" * 12
    for line in self.board:
      print '|%s|' % ''.join(line)
    print "-" * 12

  # Retorna um novo board com o mino escolhido no local especificado
  def placeMino(self, mino, column):
    lFinal = 21

    for l in range(-4, 20):
      if self.checkCollide(mino, l, column):
        lFinal = l - 1
        break

    if lFinal == 21 or self.checkCeilCollide(mino, lFinal, column):
      return False

    newBoard = Board(self)
    for i in range(len(mino.shape)):
      for j in range(len(mino.shape)):
        if mino.shape[i][j] == '#' and not (i + lFinal < 0 or i + lFinal > 19 or j + column < 0 or j + column > 9):
          newBoard.board[i+lFinal][j+column] = '#'
    
    return newBoard

  def clearAndReturnLines(self):
    linesCleared = 0

    for i in range(20):
      n = 0
      for j in range(10):
        if self.board[i][j] == '#':
          n += 1
      if n == 10:
        self.board.pop(i)
        self.board.insert(0, 10 * [' '])
        linesCleared += 1

    return linesCleared

  def addLines(self, num):
    for i in range(num):
      line = (10 * ['#'])
      line[randint(0,9)] = ' '
      self.board.append(line)
      self.board.pop(0)