You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


def perimeter (island):
  n = len(island)
  m = len(island[0])
  p = 0
  for i in range(n):
    for j in range(m):
      tmp = 4
      if (island[i][j] == 0): continue
      if (i-1 >= 0 and island[i-1][j] == 1): tmp -= 1
      if (i+1 < n and island[i+1][j] == 1): tmp -= 1
      if (j+1 < m and island[i][j+1] == 1): tmp -= 1
      if (j-1 >= 0 and island[i][j-1] == 1): tmp -= 1
      p += tmp
      
  return p
  
isl = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
 
print (per(isl))
