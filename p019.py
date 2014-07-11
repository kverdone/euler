import sys
import datetime

def main(n):
  '''
    Find how many months started on a Sunday
    between 1/1/1901 and 12/31/2000.
  '''

  cur_date = datetime.date(1901,1,1)
  count = 0

  while cur_date.year <= 2000:
    if cur_date.weekday() == 6:
      count += 1
    if cur_date.month == 12:
      cur_date = datetime.date(cur_date.year + 1, 1, 1)
    else:
      cur_date = datetime.date(cur_date.year, cur_date.month + 1, 1)

  print count


if __name__ == '__main__':
  n = 1000
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  main(n)

