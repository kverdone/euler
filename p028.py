import sys

def main(n):
  '''
    Find the sum of the diagonals of an
    n x n  matrix formed by counting by 1s 
    and moving in a clockwise spiral outwards.
    n must be odd.
  '''
  agg = 1

  for i in xrange(1,(n + 1) / 2):
    a = (2*i) ** 2 + 1
    b = (2*i + 1)**2
    c = (2*i) ** 2 - (2*i-1)
    d = (2*i)**2 + (2*i+1)

    agg += a + b + c + d

  print agg, '\a'
  
if __name__ == '__main__':
  n = 1001
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)