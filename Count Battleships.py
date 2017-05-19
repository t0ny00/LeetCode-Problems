Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.


# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


def enumerateBoats(board):
  cnt = 0
  n = len(board)
  m = len(board[0])
  for i in range(n):
    for j in range(m):
      if (board[i][j] == 'x'):
        if (i == 0 and j == 0): cnt += 1
        elif (i == 0 and not board[i][j-1] == 'x'): cnt += 1
        elif (j == 0 and not board[i-1][j] == 'x'): cnt += 1
        elif (not board[i-1][j] == 'x' and not board[i][j-1] == 'x'):cnt += 1

          
        
  return cnt
  
board = [['x','.','.','x'],['.','x','.','x'],['.','.','.','x'],['x','.','.','x']]
print (enumerateBoats(board))
