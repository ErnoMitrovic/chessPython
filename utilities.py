# utilities.py
# Ernesto and Federico
# Module that includes all the utilities for the capstone project
import random as rd

'''
  Prints the board according to a predefined board
  board: The board, which is a 2D array of ascii simbols (# for black and @ for white)
'''
def print_board(board):
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

'''
  A function that checks for any duplicated coordinates.
'''
def are_duplicates(*cordinates):
  cordinates = list(cordinates)
  for i in range(len(cordinates)):
    if cordinates.pop(0) in cordinates: return True
  return False

'''
  Makes random coordinates.
  return the random cordinates in the form of [row, column]
'''
def rand_coordinate():
  return [rd.randint(0, 7), rd.randint(0,7)]

'''
  Function that searches and finds coordinates
  return value of coordinates in the form [row, collumn], empty list otherwise.
'''
def find_piece(piece, piece_array):
  i = 0
  cordinates = []
  for row in piece_array:
    if piece in row:
      cordinates = [i, row.index(piece)]
    i += 1
  return cordinates

'''
  Used to display a 1D list of all the posible moves.
  moves: a list containing all the moves of a piece
  return the 1D list of all the moves
'''
def cords(moves):
  cordinates_list = []
  for row in moves:
    for cord in row:
      cordinates_list.append(cord)
  return cordinates_list

'''
  Checks if there is an invalid cordinate depending on the dimensions of a chess board.
  return true if there are invalid cordinates, false otherwise
'''
def invalid_cords(*cords):
  for cord in cords:
    for row_or_col in cord:
      if row_or_col < 0 or row_or_col > 7: 
        return True
  return False