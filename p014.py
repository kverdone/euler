import sys


def main(n):
  '''
    Find the longest Collatz chain
    for values less than n.
  '''
  
  max = (-1,-1)
  for n in xrange(1, n):
    if n % 100 == 0:
      print n, '\r',
    
    val = n
    steps = 1
    
    while val > 1:
      if val % 2 == 0:
        val /= 2
      else:
        val = 3 * val + 1

      steps += 1

    if steps > max[0]:
      max = (steps, n)
  print '\nMax Chain of', max[0], 'for value', max[1]

def recursively(n):
  '''
    Find the longest Collatz chain
    for values less than n.
  '''
  
  chains = {}
  max = (-1,-1)
  for n in xrange(1, n):
    if n % 25 == 0:
      print n, '\r',
    steps = collatz(n,1,chains)
    chains[n] = steps
    if steps > max[0]:
      max = (steps, n)
  print '\nMax Chain of', max, 'for value', n

def collatz(n, step, c):
  if n == 1:
    return step
  if n % 2 == 0:
    n /= 2
  else:
    n = 3 * n + 1

  if n in c.keys():
    step += c[n]
    return step

  step += 1
  step = collatz(n, step, c)
  return step


if __name__ == '__main__':
  n = 1000000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

