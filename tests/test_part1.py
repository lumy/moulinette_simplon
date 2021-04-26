import unittest
import inspect
import sys
import part1.myfuncs as part1
#import part1

BUILTINS = ['abs', 'all', 'any','ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', "__import__"]

class TestPart1(unittest.TestCase):
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
      source_code = inspect.getsource(part1).split("\n")
      self._check_rules_followed(source_code)

    def test_isalpha(self):
        self.assertTrue(part1.isalpha("abc"))
        self.assertFalse(part1.isalpha("ab2c"))
        self.assertTrue(part1.isalpha("ABC"))
        self.assertFalse(part1.isalpha("ABC#"))

    def test_isdigit(self):
        self.assertFalse(part1.isdigit("abc"))
        self.assertFalse(part1.isdigit("abc#"))
        self.assertFalse(part1.isdigit("a2bc"))
        self.assertTrue(part1.isdigit("2567"))

    def test_isalnum(self):
        self.assertFalse(part1.isalnum("abc#"))
        self.assertTrue(part1.isalnum("a2bc"))
        self.assertTrue(part1.isalnum("1234"))

    def test_lencmp(self):
        self.assertEqual(part1.lencmp("abd", "def"), 0)
        self.assertEqual(part1.lencmp("gesfsabd", "def"), 1)
        self.assertEqual(part1.lencmp("def", "gesfsabd"), -1)

    def test_tolower(self):
        self.assertEqual(part1.tolower("ABDE"), "abde")
        self.assertEqual(part1.tolower("AB#23DE"), "ab#23de")
        self.assertEqual(part1.tolower("AbCDEF1234"), "abcdef1234")

    def test_strcmp(self):
        self.assertEqual(part1.strcmp("ABC", "abc"), 0)
        self.assertEqual(part1.strcmp("abc", "abc"), 0)
        self.assertEqual(part1.strcmp("abcd", "abc"), 1)
        self.assertEqual(part1.strcmp("e", "abc"), 1)
        self.assertEqual(part1.strcmp("abcd", "fabc"), -1)
        self.assertEqual(part1.strcmp("abcd", "abcda"), -1)
