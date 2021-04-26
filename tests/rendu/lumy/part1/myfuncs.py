
def isalpha(string):
  try:
    ret = True
    for i in string:
      if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
        ret = False
    return ret
  except Exception:
    return 255

def isdigit(string):
  try:
    ret = True
    for i in string:
      if not '0' <= i <= '9':
        ret = False
    return ret
  except:
    return 255

def isalnum(string):
  try:
    ret = True
    for i in string:
      if not isdigit(i) and not isalpha(i):
        ret = False
    return ret
  except Exception:
    return 255

def tolower(string):
  ret = ""
  try:
    for s in string:
      if 'A' <= s <= 'Z':
        ret += chr(ord(s) + 32)
      else:
        ret += s
    return ret
  except:
    return 255

def _lencmp(string):
  i = 0
  for s in string:
    i += 1
  return i

def lencmp(string, string2):
  try:
    count1 = _lencmp(string)
    count2 = _lencmp(string2)
    if count1 == count2:
      return 0
    elif count1 > count2:
      return 1
    return - 1
  except:
    return 255

def strcmp(in1, in2):
  try:
    in1 = tolower(in1)
    in2 = tolower(in2)
    s = len(in1)
    if len(in1) > len(in2):
        s = len(in2)
    for i in range(s):
        if in1[i]>in2[i]:
            return 1
        if in1[i]<in2[i]:
            return -1
    if len(in1) == len(in2):
        return 0
    elif len(in1) > len(in2):
        return 1
    else:
        return -1
  except:
    return 255
