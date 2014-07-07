import sys
import math
from p003 import isPrime

def slow(n):
  '''
    Find the sum of all primes below n.
    Slow method, checking every value
    for primacy and summing.
  '''
  i = 2
  sum = 0
  while i < n:
    if isPrime(i):
      sum += i
    
    i+= 1 
  print sum

def main(n):
  '''
    Find the sum of all primes below n.
    Sieve of Eratosthenes method.
  '''
  sieve = [True] * n

  for x in xrange(2, int(n ** 0.5) + 1):
    if sieve[x]: 
      mark(sieve, x)

  print sum(i for i in xrange(2, len(sieve)) if sieve[i]) 

def mark(sieve, x):
  for i in xrange(x+x, len(sieve), x):
    sieve[i] = False


if __name__ == '__main__':
  n = 2000000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

