import sys

def main(n):
  '''
    Find the first triangular number
    that has more than n divisors
  '''
  r = 40000
  
  tri = [x*(x+1)/2 for x in xrange(1,r)] 

  sieve = [True] * r

  for x in xrange(2, int(r ** 0.5) + 1):
    if sieve[x]: 
      mark(sieve, x)  

  primes = [i for i in xrange(2,len(sieve)) if sieve[i]] 

  for num in tri:
    copy = num
    val = 1
    for prime in primes:
      count = 0 
      while copy % prime == 0:
        copy /= prime
        count += 1
      val *= count + 1
    if val > n:
      print num
      break


def mark(sieve, x):
  for i in xrange(x+x, len(sieve), x):
    sieve[i] = False


if __name__ == '__main__':
  n = 500
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

