import sys

def main(n):
  '''
    Find the total score for the names in
    names.txt where the score is calculated
    as the rank position of the name when 
    sorted times the sum of the numerical
    values of each letter.
  '''

  with open('names.txt') as f:
    names = f.read()

  names = names.split(',')
  names = [i[1:-1] for i in names]
  names.sort()

  alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
  
  agg = 0

  for i, name in enumerate(names):
    rank = i + 1
    score = sum((alpha.index(l) + 1) for l in name)
    agg += rank * score

  print agg, '\a'

if __name__ == '__main__':
  n = 10000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

