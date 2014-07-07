import sys

def main(n):
  '''
    Find the sum of all even fibonacci
    numbers as long as they are below
    the value of n.
  '''
  total = 0
  i = 1
  while True:
    val = fib(i)
    if val > n:
      break
    if val % 2 == 0:
      total += val
    i += 1
  print total

def fib(x):
  '''
    Produce the xth fibonacci number.
    Assumes starting the sequence 
    with 1,2 instead of 1,1.
  '''
  if x == 1:
    return 1
  if x == 2:
    return 1
  return fib(x-2) + fib(x-1)

if __name__ == '__main__':
  n = 4000000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

