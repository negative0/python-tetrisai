from copy import deepcopy

class Tetrominoes:
  SL = 0
  IL = 1
  ST = 2
  SQ = 3
  SI = 4
  SS = 5
  IS = 6

  minoes = [SL, IL, ST, SQ, SI, SS, IS]

  shapes = [

      [
      [' ', ' ', '#'],
      ['#', '#', '#'],
      [' ', ' ', ' ']
      ],

      [
      ['#', ' ', ' '],
      ['#', '#', '#'],
      [' ', ' ', ' ']
      ],

      [
      [' ', '#', ' '],
      ['#', '#', '#'],
      [' ', ' ', ' ']
      ],

      [
      [' ', ' ', ' ', ' '],
      [' ', '#', '#', ' '],
      [' ', '#', '#', ' '],
      [' ', ' ', ' ', ' ']
      ],

      [
      [' ', ' ', ' ', ' '],
      ['#', '#', '#', '#'],
      [' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ']
      ],

      [
      [' ', '#', '#'],
      ['#', '#', ' '],
      [' ', ' ', ' ']
      ],

      [
      ['#', '#', ' '],
      [' ', '#', '#'],
      [' ', ' ', ' ']
      ]

     ]

class Mino:
  shape = []
  mino = -1

  def __init__(self, mino):
    self.mino = mino
    self.shape = deepcopy(Tetrominoes.shapes[self.mino])

  def rotate(self):
    oldshape = deepcopy(self.shape)
    self.shape = zip(*oldshape[::-1])

  def draw(self):
    for line in self.shape:
      print '|',
      print ''.join(line),
      print '|'