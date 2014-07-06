import sys
import math

def main(n):
  total = 0
  max = -1
  for i in range(int(math.sqrt(n)), 2, -1):
    if n % i == 0 and isPrime(i):
      max = i
      break
  print max

def isPrime(x):
  for i in range(2, x//2):
    if x % i == 0:
      return False
  return True

if __name__ == '__main__':
  n = 600851475143
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

