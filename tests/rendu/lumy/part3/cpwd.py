import hashlib
from hashlib import blake2b

def check_password(password, hashed, method="sha256"):
  if method == "blake":
    return blake2b(password).hexdigest() == hashed
  m = hashlib.sha256()
  m.update(password)
  return m.hexdigest() == hashed


if __name__ == '__main__':
  check_password(b"test", "plop", "blake")
  check_password(b"Home Coming", "plop", "blake")
