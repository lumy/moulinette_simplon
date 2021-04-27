
def multiply_digit(integer):
  string = str(integer)
  res = 1
  for s in string:
    if s != '0' and s != '.':
      res *= int(s)
  return res
