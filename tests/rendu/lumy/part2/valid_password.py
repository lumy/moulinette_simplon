def has_alpha(string):
  for i in string:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
      return True
  return False

def has_digit(string):
  for i in string:
    if '0' <= i <= '9':
      return True
  return False

def has_special(string):
  for i in string:
    if not '0' <= i <= '9' and not 'a' <= i <= 'z' or 'A' <= i <= 'Z':
      return True
  return False

def valid_password(string):
  return all((len(string) > 8,
             has_digit(string),
             has_alpha(string),
             has_special(string))
  )
