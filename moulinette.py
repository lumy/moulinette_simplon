import argparse, os

# it would be nice to have a dynamique load so that would be perfectly generique and usable for each exam (providing a csv by exam)

def verify_csv_content(line):
  """Verify that csv file content is formated as excepted"""
  if len(line.split(',')) != 2:
    return False
  return True

def read_csv_file(filename):
  """Read csv file and return list of file to import"""
  with open(filename, 'r') as f:
    content = f.readlines()
  if not all([verify_csv_content(x) for x in content]):
    msg = "CSV content unexcepted. Content should (by line) name,filepath,"
    print(msg)
    raise ValueError(msg)
  return [c.strip().split(',') for c in content]

def init_argparse():
  """Init ArgParser"""
  parser = argparse.ArgumentParser(description="""Moulinette to check exam. Based on csv file it will import and run test""")
  parser.add_argument('csv', metavar='s', type=str,
                    help='csv file to read python unittest file')
  parser.add_argument('rendu', metavar='r', type=str,
                    help='Folder containing all student works (each folder should be a group/student)')
  return parser

def prepare_context():
  pass
def unload_context():
  pass

def correction(list_to_imp, root_students_folder):
  """For each student apply list_to_imp"""
  for student_folder in  os.listdir(root_students_folder):
    for to_imp in list_to_imp:
      prepare_context()
      print("Testing Student {} for {}".format(student_folder, to_imp[0]))
      unload_context()

def main():
  """EntryPoint"""
  parser = init_argparse()
  args = parser.parse_args()
  list_to_import = read_csv_file(args.csv)
  correction(list_to_import, args.rendu)


if __name__ == '__main__':
  main()
