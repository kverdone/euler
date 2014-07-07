import sys
import math

def main():
  '''
    Find the greatest 6 digit palindromic
    number that is a product of two three
    digit numbers.
  '''
  for i in range(999,99,-1):
    temp = str(i)
    pal = int(temp + temp[::-1])
    if threeDigDiv(pal):
      print pal
      break

def threeDigDiv(x):
  '''
    Iterates and finds if a given x is
    divisible by three digit numbers.
  '''
  val = int(math.sqrt(x))
  for i in range(val, 100, -1):
    if (x % i == 0) and (999 >= x // i >= 100):
      print x, i, x//i
      return True
  return False

if __name__ == '__main__':
  main()

