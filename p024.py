import sys
import itertools

def main(n):
  '''
    Find the nth lexicographic permuations of
    the digits 0 to 9.
  '''
  lst = range(10)

  p = itertools.permutations(lst)

  agg = 0

  val = ''

  for i, entry in enumerate(p):
    if i == n-1:
      for char in entry:
        val += str(char)
      print int(val)
      break

  print '\a'

if __name__ == '__main__':
  n = 1000000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

