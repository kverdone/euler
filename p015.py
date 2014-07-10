import sys
from math import factorial

def main(n):
  '''
    Find the number of paths to traverse an
    n by n grid moving only down and right,
    moving from top left to bottom right
    corner.
  '''
  
  row = 2 * n
  col = n
  paths = factorial(row) / (factorial(col) * factorial(row - col))

  print row, 'choose', col, ' = ', paths



if __name__ == '__main__':
  n = 20
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

