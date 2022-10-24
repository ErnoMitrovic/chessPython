# pieces.py
# Ernesto and Federico
# Module that contains the methods for the pieces of the project

'''
  Checks if the cordinates generated hold true for a valid kings distribution
  K_cord: cordinates of the white king
  k_cord: cordinates of the black king
  returns: True if it's valid, False otherwise
'''
def valid_king(K_cord, k_cord):
  for row in king_moves(K_cord):
    if k_cord in row: return False
  return True

'''
  Builds a valid list of all the moves that the king has, this function works also when the king is at the edges of the board.
  cord: the cordinates of the king
  return: The moves according to the position of the king in the board.
'''
def king_moves(cord):
  moves = []
  for row in range(cord[0]-1, cord[0]+2):
    cond_row = row >= 0 and row <= 7
    moves_row = []
    for col in range(cord[1]-1, cord[1]+2):
      cond_col = col >= 0 and col <= 7
      if row == cord[0] and col == cord[1]: 
        continue
      elif cond_row and cond_col:
        moves_row.append([row, col])
    moves.append(moves_row)
  return moves

'''
  Builds the horizontal moves for the queen according to a specific position of the white queen and the white king.
  Q_cord: cordinates of the white queen
  K_cord: cordinates of the white king
  return: horizontal moves of the queen
'''
def horizontal_Q(Q_cord, K_cord):
  row_Q, col_Q = Q_cord
  row_K, col_K = K_cord
  horizontalMoves = []
  for col in range(col_Q + 1, 8):
    if col == col_K and row_Q == row_K:
      break
    horizontalMoves.append([row_Q, col])
  for col in range(col_Q - 1, - 1, -1):
    if col == col_K and row_Q == row_K:
      break
    horizontalMoves.append([row_Q, col])
  return horizontalMoves
  
'''
  Builds the vertical moves for the queen according to a specific position of the white queen and the white king.
  Q_cord: cordinates of the white queen
  K_cord: cordinates of the white king
  return: vertical moves of the queen
'''
def vertical_Q(Q_cord, K_cord):
  row_Q = Q_cord[0]
  row_K, col_K = K_cord
  vertical_moves = []
  for row in range(row_Q - 1, -1, -1):
    if row == row_K and Q_cord[1] == col_K:
      break
    vertical_moves.append([row, Q_cord[1]])
  for row in range(row_Q + 1, 8):
    if row == row_K and Q_cord[1] == col_K:
      break
    vertical_moves.append([row, Q_cord[1]])
  return vertical_moves

'''
  Builds the diagonal moves for the queen according to a specific position of the white queen and the white king.
  Q_cord: cordinates of the white queen
  K_cord: cordinates of the white king
  return: diagonal moves of the queen
'''
def diagonal_Q(Q_cord, K_cord):
  lim_pos = 7
  lim_neg = 0
  start_row, start_col = Q_cord
  row_K, col_K = K_cord
  cuadrant = 1
  moves = []
  while cuadrant < 5:
    if cuadrant == 1:
      while start_row > lim_neg and start_col < lim_pos and not (row_K == start_row and col_K == start_col):
        start_row -= 1
        start_col += 1
        moves.append([start_row, start_col])
      cuadrant += 1
      start_row, start_col = Q_cord
    elif cuadrant == 2: 
      while start_row > lim_neg and start_col > lim_neg and not (row_K == start_row and col_K == start_col):
        start_row -= 1
        start_col -= 1
        moves.append([start_row, start_col])
      cuadrant += 1
      start_row, start_col = Q_cord
    elif cuadrant == 3: 
      while start_row < lim_pos and start_col > lim_neg and not (row_K == start_row and col_K == start_col):
        start_row += 1
        start_col -= 1
        moves.append([start_row, start_col])
      cuadrant += 1
      start_row, start_col = Q_cord
    elif cuadrant == 4: 
      while start_row < lim_pos and start_col < lim_pos and not (row_K == start_row and col_K == start_col):
        start_row += 1
        start_col += 1
        moves.append([start_row, start_col])
      cuadrant += 1
  return moves

'''
  Builds the moves for the queen according to a specific position of the white queen and the white king.
  Q_cord: cordinates of the white queen
  K_cord: cordinates of the white king
  return: moves of the queen
'''
def Q_moves(Q_cord, K_cord):
  moves = []
  moves.append(horizontal_Q(Q_cord, K_cord))
  moves.append(vertical_Q(Q_cord, K_cord))
  moves.append(diagonal_Q(Q_cord, K_cord))
  return moves
