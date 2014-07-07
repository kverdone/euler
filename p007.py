import sys
from p003 import isPrime

def main(n):
  '''
    Find the nth prime number
  '''
  i = 2
  counter = 0
  while True:
    if isPrime(i):
      counter += 1
      if counter == n:
        print i
        break
    i += 1

if __name__ == '__main__':
  n = 10001
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

