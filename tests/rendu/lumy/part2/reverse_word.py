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

def reverse_word(string):
  list_s = split(string)
  ret = []
  for s in list_s:
    ret += [ s[::-1] ]
  s_ret = ""
  for i in ret:
    s_ret += i
    s_ret += " "
  return s_ret[:-1]
