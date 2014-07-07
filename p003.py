import sys
import math

def main(n):
  '''
    Find the largest prime factor
    of a given number n.
  '''
  total = 0
  start = int(math.sqrt(n))
  for i in range(start, 2, -1):
    if n % i == 0 and isPrime(i):
      print i
      break

def isPrime(x):
  '''
    Iterates looking for any factors.
    If found, returns false.
  '''
  if x in (2,3):
    return True
  for i in range(2, x//2+1):
    if x % i == 0:
      return False
  return True

if __name__ == '__main__':
  n = 600851475143
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

