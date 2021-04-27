import unittest
import inspect
import sys
from part2 import three_word, reverse_word
from part2 import fizzbuzz, syracuse
from part2 import valid_password, multiply_digit

BUILTINS = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', "__import__"]

class TestPart2(unittest.TestCase):
  def tearDown(self):
    """Should be implemented in every Test easier than doing it in unload_context"""
    try:
      del sys.modules['part2.three_word']
      del sys.modules['part2.reverse_word']
      del sys.modules['part2.fizzbuzz']
      del sys.modules['part2.valid_password']
      del sys.modules['part2.multiply_digit']
      del sys.modules['part2.syracuse']
      del sys.modules['part2']
    except:
      pass
    return super(TestPart2, self).tearDown()

  def _check_rules_followed(self, text):
    """For now it's a basic check but it would be nice to have a real regex more powerfull"""
    for index, line in enumerate(text):
      if "import" in line:
        print("ELIMINATED: Usage of Import line[%s]: %s" % (index, line))
        #raise ValueError("Eliminated for not followed the rule")
      if '.' in line:
        print("ELIMINATED: methods Used line[%s]: %s" % (index, line))
        #raise ValueError("Eliminated for not followed the rule")

  def count_builtins(self, text):
    bonus = 0
    for index, line in enumerate(text):
      if any([" %s(" % builtin in line for builtin in BUILTINS]):
        print("Usage of Builtin line[%s]: %s" % (index, line))
        bonus += 1
    return bonus

  def _test_unauthorized_code(self, module_name):
      source_code = inspect.getsource(module_name).split("\n")
      self._check_rules_followed(source_code)
      return self.count_builtins(source_code)
  def test_unauthorized_and_bonus(self):
    bonus = 0
    for i in [three_word, reverse_word, fizzbuzz, valid_password, multiply_digit, syracuse]:
      bonus += self._test_unauthorized_code(i)
    print("BONUS: %s" % bonus)

  def test_threeword(self):
    self.assertTrue(three_word.three_word("abc bce def"))
    self.assertTrue(three_word.three_word("a@bc bce def gef"))
    self.assertFalse(three_word.three_word("a@bc f gef"))
    self.assertFalse(three_word.three_word("a@bc f gef  "))
    self.assertFalse(three_word.three_word("abc 1 gef"))

  def test_revword(self):
    self.assertEqual(reverse_word.reverse_word("abc bce def"), "cba ecb fed")
    self.assertEqual(reverse_word.reverse_word("hello world"), "olleh dlrow")

  def test_valid_password(self):
    self.assertTrue(valid_password.valid_password("Th3seIs@S3CureP@swd"))
    self.assertFalse(valid_password.valid_password("wd"))
    self.assertFalse(valid_password.valid_password("abcdefghijkl"))
    self.assertFalse(valid_password.valid_password("1234567890"))
    self.assertFalse(valid_password.valid_password("123456abcdefh"))
    self.assertFalse(valid_password.valid_password("@#!$@#"))

  def test_multiply(self):
    self.assertEqual(multiply_digit.multiply_digit("123"), 6)
    self.assertEqual(multiply_digit.multiply_digit("10203"), 6)
    self.assertEqual(multiply_digit.multiply_digit("12203"), 12)
    self.assertEqual(multiply_digit.multiply_digit("0900"), 9)
    self.assertEqual(multiply_digit.multiply_digit("09019"), 81)

  def test_syracuse(self):
    self.assertEqual(syracuse.syracuse(7), [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

  def test_fizzbuzz(self):
    self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")
    self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
    self.assertEqual(fizzbuzz.fizzbuzz(15), "Fizz Buzz")
    self.assertEqual(fizzbuzz.fizzbuzz(2), "2")
