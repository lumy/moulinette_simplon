import sys, json

def mwrite(k, v):
  try:
    with open("mydb.db", "r") as f:
      content = json.load(f)
  except:
    content = {}
  content[k] = v
  with open("mydb.db", "w") as f:
    json.dump(content, f)

def mget(k):
  with open("mydb.db", "r") as f:
    content = json.load(f)
    print(content[k])

def main():
  if sys.argv[1] == "add":
    mwrite(sys.argv[2], sys.argv[3])
  if sys.argv[1] == "get":
    mget(sys.argv[2])

main()
