import sys

def main(n):
  '''
    What term of the fibonnaci sequence is
    the first to have n digits.
  '''
  
  fib = [1,1]

  while len(str(fib[-1])) < n:
    fib.append(fib[-1] + fib[-2])
  print len(fib), '\a'

if __name__ == '__main__':
  n = 1000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

