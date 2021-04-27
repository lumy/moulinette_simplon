import unittest
import inspect
import sys
from part1 import myfuncs


BUILTINS = ['abs', 'all', 'any','ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', "__import__"]

class TestMyfuncs(unittest.TestCase):
    def tearDown(self):
      """Should be implemented in every Test easier than doing it in unload_context"""
      try:
        del sys.modules['part1.myfuncs']
      except:
        pass
      try:
        del sys.modules['part1']
      except:
        pass

      return super(TestMyfuncs, self).tearDown()

    def _check_rules_followed(self, text):
      """For now it's a basic check but it would be nice to have a real regex more powerfull"""
      authorized = ["len", "range", "ord", "chr"]
      unauthorized_builtins = ["%s(" % b for b in BUILTINS if b not in authorized]
      for index, line in enumerate(text):
        if "import" in line:
          print("ELIMINATED: Usage of Import line[%s]: %s" % (index, line))
          #raise ValueError("Eliminated for not followed the rule")
        if any([builtin in line for builtin in unauthorized_builtins]):
          print("ELIMINATED: Builtin Used line[%s]: %s" % (index, line))
          #raise ValueError("Eliminated for not followed the rule")
        if '.' in line:
          print("ELIMINATED: methods Used line[%s]: %s" % (index, line))
          #raise ValueError("Eliminated for not followed the rule")

    def test_unauthorized_code(self):
      source_code = inspect.getsource(myfuncs).split("\n")
      self._check_rules_followed(source_code)

    def test_bonus(self):
      """TODO"""
      self.assertEqual(myfuncs.isalpha(123), 255)
      self.assertEqual(myfuncs.isalpha([1, 2, 3]), 255)
      self.assertEqual(myfuncs.isdigit(123), 255)
      self.assertEqual(myfuncs.isdigit([1,2,3]), 255)
      self.assertEqual(myfuncs.isalnum(124), 255)
      self.assertEqual(myfuncs.isalnum(124.2), 255)
      self.assertEqual(myfuncs.lencmp(123, "def"), 255)
      self.assertEqual(myfuncs.lencmp("def", 123), 255)
      self.assertEqual(myfuncs.tolower(123), 255)
      self.assertEqual(myfuncs.tolower(3213.231), 255)
      self.assertEqual(myfuncs.strcmp(123, "abc"), 255)
      self.assertEqual(myfuncs.strcmp("abc", [1,2,3]), 255)

    def test_isalpha(self):
        self.assertTrue(myfuncs.isalpha("abc"))
        self.assertFalse(myfuncs.isalpha("ab2c"))
        self.assertTrue(myfuncs.isalpha("ABC"))
        self.assertFalse(myfuncs.isalpha("ABC#"))

    def test_isdigit(self):
        self.assertFalse(myfuncs.isdigit("abc"))
        self.assertFalse(myfuncs.isdigit("abc#"))
        self.assertFalse(myfuncs.isdigit("a2bc"))
        self.assertTrue(myfuncs.isdigit("2567"))

    def test_isalnum(self):
        self.assertFalse(myfuncs.isalnum("abc#"))
        self.assertTrue(myfuncs.isalnum("a2bc"))
        self.assertTrue(myfuncs.isalnum("1234"))

    def test_lencmp(self):
        self.assertEqual(myfuncs.lencmp("abd", "def"), 0)
        self.assertEqual(myfuncs.lencmp("gesfsabd", "def"), 1)
        self.assertEqual(myfuncs.lencmp("def", "gesfsabd"), -1)

    def test_tolower(self):
        self.assertEqual(myfuncs.tolower("ABDE"), "abde")
        self.assertEqual(myfuncs.tolower("AB#23DE"), "ab#23de")
        self.assertEqual(myfuncs.tolower("AbCDEF1234"), "abcdef1234")

    def test_strcmp(self):
        self.assertEqual(myfuncs.strcmp("ABC", "abc"), 0)
        self.assertEqual(myfuncs.strcmp("abc", "abc"), 0)
        self.assertEqual(myfuncs.strcmp("abcd", "abc"), 1)
        self.assertEqual(myfuncs.strcmp("e", "abc"), 1)
        self.assertEqual(myfuncs.strcmp("abcd", "fabc"), -1)
        self.assertEqual(myfuncs.strcmp("abcd", "abcda"), -1)
