
def split(s):
  r = []
  current = ""
  for i in s:
    if i == " ":
      if current != "":
        r += [current]
      current = ""
    else:
      current += i
  if current != "":
    r += [current]
  return r

def isalpha(strng):
  ret = True
  for i in strng:
    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
      ret = False
  return ret

def three_word(string):
  list_string = split(string)
  counter = 0
  for string in list_string:
    if isalpha(string):
      counter += 1
    else:
      counter = 0
    if counter >= 3:
      return True
  return False
