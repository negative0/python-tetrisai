from copy import deepcopy

class BoardScorer:
  params = []

  def __init__(self, params):
    self.params = deepcopy(params)

  def scoreBoard(self, board):
    linesSent = 0

    score = 0
    score += self.params[0][0] * pow(float(board.linesCleared), float(self.params[0][1])) 
    score += self.params[1][0] * pow(float(self.m_surface(board)), float(self.params[1][1])) 
    score += self.params[2][0] * pow(float(self.m_pits(board)), float(self.params[2][1])) 
    score += self.params[3][0] * pow(float(self.m_height(board)), float(self.params[3][1])) 
    score += self.params[4][0] * pow(float(self.m_holes(board)), float(self.params[4][1])) 
    score += self.params[5][0] * pow(float(board.streak), float(self.params[5][1])) 

    return score


  # Metricas utilizadas sao definidas abaixo. Nao ha normalizacao.

  # Maior altura ocupada do board
  def m_height(self, board):
    height_p = 0

    for i in range(20):
      for j in range(10):
        if board.board[i][j] == '#':
          height_p += (20 - i)
    return height_p

  # Espacos vazios sob espacos ocupados no board
  def m_holes(self, board):
    holes = 0
    mask = [" "] * 10
    for i in range(20):
      for j in range(10):
        if board.board[i][j] == ' ' and mask[j] == '#':
          holes += 1
        elif board.board[i][j] == '#' and mask[j] == ' ':
          mask[j] = '#'
    return holes

  # Espacos em "buracos" de largura 1
  def m_pits(self, board):
    pits = 0
    for j in range(10):
      cmul = 0
      cpit = 0

      for i in range(20):
        if board.getPos(i, j) == ' ' and board.getPos(i, j-1) == '#' and board.getPos(i, j+1) == '#':
          cmul = 1

        if cmul == 1 and board.getPos(i, j) == ' ':
          cpit += 1

        if cmul == 1 and board.getPos(i, j) == '#':
          break

      pits += cpit

    return pits
  
  # Superficie delimitada pelos minos no board
  def m_surface(self, board):
    surface = 0
    for i in range(20):
      for j in range(10):
        if board.board[i][j] == '#':
          if i == 0 or i == 19:
            surface += 1
          else:
            surface += 1 if board.board[i-1][j] == ' ' else 0
            surface += 1 if board.board[i+1][j] == ' ' else 0
  
          if j == 0 or j == 9:
            surface += 1
          else:
            surface += 1 if board.board[i][j-1] == ' ' else 0
            surface += 1 if board.board[i][j+1] == ' ' else 0
    return surface