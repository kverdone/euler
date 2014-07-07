import sys
import math

def main(x):
  '''
    Find a pythagorean triple where the sum
    of the legs is equal to x.
  '''
  a = -1
  c = -1
  b = 3
  sum = -1
  while sum != x:
    if b % 2 == 1:
      mn = 2 * b
      odd = True
    else:
      mn = b / 2
      odd = False
    lst = facPairs(mn)

    for m,n in lst:
      a = abs(m ** 2 - n ** 2)
      c = abs(m ** 2 + n ** 2)
      if odd:
        a /= 2
        c /= 2
      sum = a + b + c

      if sum == x:
        print a, b, c
        print a*b*c
        break

    b += 1

def facPairs(mn):
  lst = []
  for i in range(1, int(math.sqrt(mn))+1):
    if mn % i == 0:
      lst.append((i,mn/i))
  return lst

if __name__ == '__main__':
  n = 1000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

