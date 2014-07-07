import sys
from p003 import isPrime

def main(n):
  '''
    Find the smallest number evenly divisble
    by all numbers from 1 to n
  '''
  prod = 1
  factors = {}
  for i in range(2, n+1):
    for j in range(2,i):
      print i,j
      if isPrime(j):
        if j not in factors.keys():
          factors[j] = 1
        else:
          factors[j] += i//j - factors[j]
  print factors

  for i in factors.keys():
    prod *= i ** factors[i]
  #prod *= i
  print prod

if __name__ == '__main__':
  n = 20
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

