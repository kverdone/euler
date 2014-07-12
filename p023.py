import sys

def main(n):
  '''
    Find the sum of all numbers that cannot be
    expressed as the sum of two abundant numbers
    below n.
  '''

  abundant = []
  agg = 0

  for i in xrange(1,n):
    divs = sum(d for d in xrange(1,i) if i % d == 0)
    if divs > i:
      abundant.append(i)

  flag = False

  s = [x + y for x in abundant for y in abundant if x + y < n]
  s = set(s)

  for i in xrange(1,n):
    if i in s:
      continue
    else:
      agg += i

  print agg, '\a'

if __name__ == '__main__':
  n = 28124
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

