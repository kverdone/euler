import sys

def main(n):
  '''
    Find all amicable numbers below n where
    a amicable numbers are defined as pairs
    of numbers where the sum of one's 
    proper divisors is equal to the other
    number.
  '''

  agg = 0

  for x in xrange(1,n):
    d_a = sum(i for i in xrange(1,x) if x % i == 0)
    if d_a < n and d_a != x:
      d_b = sum(i for i in xrange(1,d_a) if d_a % i == 0)
      #print x, xsum, am_sum
      if x == d_b:
        agg += x

  print agg, '\a'

if __name__ == '__main__':
  n = 10000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

