import unittest
from part1 import myfuncs

class TestPart1(unittest.TestCase):
  def tearDown(self):
    """Should be implemented in every Test easier than doing it in unload_context"""
    try:
      del sys.modules['part1']
    except:
      pass
    try:
      del sys.modules['part1.myfuncs']
    except:
      pass
    return super(TestPart1, self).tearDown()

  def test_isalpha(self):
    self.assertEqual(myfuncs.isalpha(123), 255)
    self.assertEqual(myfuncs.isalpha([1, 2, 3]), 255)

  def test_isdigit(self):
    self.assertEqual(myfuncs.isdigit(123), 255)
    self.assertEqual(myfuncs.isdigit([1,2,3]), 255)

  def test_isalnum(self):
    self.assertEqual(myfuncs.isalnum(124), 255)
    self.assertEqual(myfuncs.isalnum(124.2), 255)

  def test_lencmp(self):
    self.assertEqual(myfuncs.lencmp(123, "def"), 255)
    self.assertEqual(myfuncs.lencmp("def", 123), 255)

  def test_tolower(self):
    self.assertEqual(myfuncs.tolower(123), 255)
    self.assertEqual(myfuncs.tolower(3213.231), 255)

  def test_strcmp(self):
    self.assertEqual(myfuncs.strcmp(123, "abc"), 255)
    self.assertEqual(myfuncs.strcmp("abc", [1,2,3]), 255)
