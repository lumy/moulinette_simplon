import argparse, os, sys
import unittest
import importlib
# it would be nice to have a dynamique load so that would be perfectly generique and usable for each exam (providing a csv by exam)

def verify_csv_content(line):
  """Verify that csv file content is formated as excepted"""
  if len(line.split(',')) != 4:
    return False
  return True

def read_csv_file(filename):
  """Read csv file and return list of file to import"""
  with open(filename, 'r') as f:
    content = f.readlines()
  if not all([verify_csv_content(x) for x in content]):
    msg = "CSV content unexcepted. Content should (by line) folder,reference(name for print),filepath,filename"
    print(msg)
    raise ValueError(msg)
  return [c.strip().split(',') for c in content]

def init_argparse():
  """Init ArgParser"""
  parser = argparse.ArgumentParser(description="""Moulinette to check exam. Based on csv file it will import and run test""")
  parser.add_argument('csv', metavar='csv', type=str,
                    help='csv file to read python unittest file')
  parser.add_argument('rendu', metavar='rendu', type=str,
                    help='Folder containing all student works (each folder should be a group/student)')
  parser.add_argument('--debug', '-d', metavar='--debug', action='store_const', const=True,
                    help='debug mode')
  return parser

def prepare_context(to_imp, root_student_folder):
  sys.path.insert(0, root_student_folder)
  try:
    module_exam = importlib.import_module("%s.%s" % (to_imp[2], to_imp[3]))
    module_exam = importlib.reload(module_exam)
  except ModuleNotFoundError:
    return None, None
  module_name = to_imp[0]
  return module_exam, module_name

def unload_context(to_imp, module_exam):
  #print(sys.modules)
  try:
    del sys.modules[to_imp[0]]
    del sys.modules[to_imp[0].split('.')[0]]
  except KeyError:
    pass
  #del sys.modules[str(module_exam.__name__)]
  #del module_exam
  sys.path.pop(0)

def run_unittest(module_exam, module_name):
  suite = unittest.TestLoader().loadTestsFromModule(module_exam)
  result = unittest.TextTestRunner().run(suite)
  score = result.testsRun - len(result.errors) - len(result.failures)
  return (result.testsRun, score)


def correction(list_to_imp, root_students_folder):
  """For each student apply list_to_imp"""
  for student_folder in  os.listdir(root_students_folder):
    print("Testing Student {}".format(student_folder))
    for to_imp in list_to_imp:
      msg = "Test {}:".format(to_imp[1])
      module_exam, module_name = prepare_context(to_imp, os.path.join(root_students_folder, student_folder))
      if module_exam:
        max, score = run_unittest(module_exam, module_name)
        msg = "%s Score %s/%s" % (msg, score, max)
      else:
        msg += " could not be loaded at path %s. Score: 0" % to_imp[2]
      print(msg)
      unload_context(to_imp, module_exam)


def main():
  """EntryPoint"""
  parser = init_argparse()
  args = parser.parse_args()
  if not args.debug:
    sys.stderr = open(os.devnull, 'w')
  list_to_import = read_csv_file(args.csv)
  correction(list_to_import, args.rendu)


if __name__ == '__main__':
  main()
