import sys

def main(n):
  '''
    Find the sum of the digits in 2 to the n.
  '''

  val = 2 ** n
  sm = sum(int(digit) for digit in str(val))
  
  print "Sum of digits in"
  print val
  print "is equal to"
  print sm


if __name__ == '__main__':
  n = 1000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

