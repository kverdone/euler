import sys
import math

def main(n):
  '''
    Find the sum of the digits of n factorial.
  '''

  agg = sum(int(x) for x in str(math.factorial(n)))
  
  print agg, '\a'

if __name__ == '__main__':
  n = 100
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

