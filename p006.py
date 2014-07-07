import sys

def main(n):
  '''
    Find the difference between the
    square of the sum and the sum of 
    the squares of the first n numbers.
  '''
  sq_sums = (n * (n + 1) / 2) ** 2
  sum_sqs = n * (n + 1) * (2 * n + 1) / 6
  print sq_sums, sum_sqs
  print sq_sums - sum_sqs

if __name__ == '__main__':
  n = 100
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

