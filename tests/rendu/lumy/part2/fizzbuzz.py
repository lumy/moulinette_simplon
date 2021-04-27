
def fizzbuzz(intger):
  r = ""
  if intger % 3 == 0:
    r += "Fizz"
  if intger % 5 == 0:
    if r != "":
      r += " "
    r += "Buzz"
  if r == "":
    return str(intger)
  return r
