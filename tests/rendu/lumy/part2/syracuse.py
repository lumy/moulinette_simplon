
def syracuse(integer):
  ret = []
  while integer != 1:
    if integer % 2 == 0:
      integer = int(integer / 2)
    else:
      integer *= 3
      integer += 1
    ret += [integer]
  return ret
