# Not for delivery
from capstone_project import utilities as util
from capstone_project import pieces as piece
import math as m


def queenMatrix(cord):
  matQ = []
  for row in range(8):
    matRow = []
    for col in range(8):
      if row == cord[0] and col == cord[1]:
        matRow.append('Q')
      elif row == cord[0] or col == cord[1] or util.is_diagonal(cord[0], cord[1], row, col): 
        matRow.append([row, col])
    matQ.append(matRow)
  return matQ

def queenMatrixFixed(QMat, K_cord):
  QRow, QCol = util.find_piece('Q', QMat)
  KRow, KCol = K_cord

  if QRow == KRow:
    deltaCol = KCol - QCol
    if deltaCol > 0:
      QMat[QRow] = QMat[QRow][:KCol]
    else:
      QMat[QRow] = QMat[QRow][KCol:]

  elif QCol == KCol:
    deltaRow = KRow - QRow
    if deltaRow > 0:
      for row_Q in QMat[QRow + 1:]:
        for cords in row_Q:
          if cords[0] >= QRow + deltaRow and cords[1] == QCol:
            row_Q.remove(cords)
    else:
      for row_Q in QMat[:KRow+1]:
        for cords in row_Q:
          if cords[0] <= QRow + deltaRow and cords[1] == QCol:
            row_Q.remove(cords)

  elif util.is_diagonal(QRow, QCol, KRow, KCol):
    deltaRow = KRow - QRow
    deltaCol = KCol - QCol
    if deltaRow > 0 and deltaCol > 0:
      for row_Q in QMat[QRow+1:]:
        for cords in row_Q:
          if cords[0] >= QRow + deltaRow and cords[1] >= QCol + deltaCol:
            row_Q.remove(cords)
    elif deltaRow > 0 and deltaCol < 0:
      for Q in QMat[QRow + 1:]:
        for cords in row_Q:
          if cords[0] >= QRow + deltaRow and cords[1] <= QCol + deltaCol:
            row_Q.remove(cords)
    elif deltaRow < 0 and deltaCol < 0:
      for row_Q in QMat[:KRow + 1]:
        for cords in row_Q:
          if cords[0] <= QRow + deltaRow and cords[1] <= QCol + deltaCol:
            row_Q.remove(cords)
    else:
      for row_Q in QMat[:KRow + 1]:
        for cords in row_Q:
          if cords[0] <= QRow + deltaRow and cords[1] >= QCol + deltaCol:
            row_Q.remove(cords)
  return QMat


def conditions_input(board):
  y = 0
  k_count = 0
  K_count = 0
  for row in board:
    if 'K' in row: 
      K = [y, row.index('K')]
      K_count += 1
    if 'k' in row: 
      k = [y, row.index('k')]
      k_count += 1
  if k_count > 1 or K_count > 1 or not piece.valid_king(K, k): return False
  return True

def is_diagonal(row, col, rowf, colf):
  return True if m.fabs(rowf - row) == m.fabs(colf - col) else False