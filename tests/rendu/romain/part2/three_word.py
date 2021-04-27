
def isalpha(i):
  return 'a' <= i <= 'z' or 'A' <= i <= 'Z'

def three_word(string):
  word = 0
  word_started = False
  for i in string:
    if isalpha(i) and not word_started:
      word_started = True
    elif not isalpha(i) and word_started:
      word_started = False
  return None
