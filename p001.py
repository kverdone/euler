import sys

def main(n):
  '''
    Iterate through the numbers.
    If a number is divisible by 3 or 5, add 
    it to the total. If this occurs, jump 
    to to the next loop to avoid double
    counting.
  '''
  total = 0
  for i in range(1, n):
    if i % 3 == 0:
      total += i
      continue
    if i % 5 == 0:
      total += i
      continue
  print total

if __name__ == '__main__':
  n = 1000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

