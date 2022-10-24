# capstone.py
# Ernesto and Federico
# Generate a chess board with positions to determine if the black king is in checkmante or not, and its possible moves. The only pieces are white king and queen, and black king.

from capstone_project import utilities as util
from capstone_project import pieces as piece

'''
  Creates an empty board
  return an 8 x 8 board
'''
def empty_board():
  board = []
  shape = '@'
  for row in range(8):
    rowBoard = []
    for col in range(8):
      rowBoard.append(shape)
      if col < 7:
        if shape == '@':
          shape = '#'
        else:
          shape = '@'
    board.append(rowBoard)
  return board

'''
  Function that detects is the user wants to get random positions, enter a complete valid board, or wants to put specific coordinates.
  return the board according to user specification
'''
def menu():
  option = int(input())
  if option == 1: return random_board()
  elif option == 2: return user_board()
  elif option == 3: return input_positions()
  else: print("Only enter 1, 2 or 3")

'''
  Function used to generate random coordinates for each piece and checks if the board is valid
  return the board
'''
def random_board():
  board = empty_board()
  Q, K, k = (util.rand_coordinate() for i in range(3))
  while (util.are_duplicates(Q, K, k) 
  or not piece.valid_king(K, k)):
    Q, K, k = (util.rand_coordinate() for i in range(3))
  board[Q[0]][Q[1]] = 'Q'
  board[K[0]][K[1]] = 'K'
  board[k[0]][k[1]] = 'k'
  return board

'''
  Function used to generate board accoding to the users input, checking that it's a valid board.
  return the board
'''
def user_board():
  board = []
  for row in range(8):
    board.append(input())
  board = [row.strip().split() for row in board]
  if not conditions_input(board):
    print() 
    board = user_board()
  return board

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
    y+=1
  if k_count > 1 or K_count > 1 or not piece.valid_king(K, k): return False
  return True

'''
  Function used IF the user wants to put their own coordinates.
  return the board with the inserted pieces.
'''
def input_positions():
  board = empty_board()
  print("Put the cordinates of the White King (row, collumn)")
  K = [int(input()) for i in range(2)]
  print("Put the cordinates of the White Queen (row, collumn)")
  Q = [int(input()) for i in range(2)]
  print("Put the cordinates of the Black King (row, collumn)")
  k = [int(input()) for i in range(2)]
  board[K[0]][K[1]] = 'K'
  board[Q[0]][Q[1]] = 'Q'
  board[k[0]][k[1]] = 'k'
  if (not piece.valid_king(K, k) 
  or util.are_duplicates(K, Q, k) 
  or util.invalid_cords(K, k, Q)):
    print("Invalid input, do it again")
    board = input_positions()
  return board

'''
  Checks moves that the black king can do using the coordinates from the other pieces.
  Q_moves: white queen movements
  K_moves: white king moves
  k_matrix: black king moves
  return: list of moves for the black king
'''
def black_king_moves(Q_moves, K_moves, k_matrix):
  Q_cords = util.cords(Q_moves)
  K_cords = util.cords(K_moves)
  k_cords = util.cords(k_matrix)
  return [cords 
  for cords in k_cords
   if cords not in Q_cords 
   and cords not in K_cords]

'''
  Checks if there's a check with any of the possible moves that the queen can do.
  Q_moves: moves of the queen
  k_cord: cordinates of the black king
  returns true if the k is in the moves of the queen (is in check)
'''
def is_check(Q_moves, k_cord):
  for row_Q in Q_moves:
    if k_cord in row_Q : 
      return True
  return False

'''
  Checks if the black King is in checkmate.
  Q_moves: The moves of the white queen
  K_moves: The moves of the white king
  k_moves: The moves of the black king
  k_cord: the cordinates of the black king
  returns true if the black king is in check and has no other moves
'''
def is_checkmate(Q_moves, K_moves, k_moves, k_cord):
  if (is_check(Q_moves, k_cord) 
  and not black_king_moves(Q_moves, K_moves, k_moves)):
    return True
  return False

'''Makes everything run'''
def execution():
  board = menu()
  print()
  util.print_board(board)
  k_cord = util.find_piece('k', board)
  K_cord = util.find_piece('K', board)
  Q_cord = util.find_piece('Q', board)
  Q_moves = piece.Q_moves(Q_cord, K_cord)
  K_matrix = piece.king_moves(K_cord)
  k_matrix = piece.king_moves(k_cord)
  print(black_king_moves(Q_moves, K_matrix, k_matrix))
  print("Check:", is_check(Q_moves, k_cord))
  print("Checkmate:", is_checkmate(Q_moves, K_matrix, k_matrix, k_cord))