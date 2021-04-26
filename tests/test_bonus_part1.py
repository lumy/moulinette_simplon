import unittest
import part1.myfuncs as part1

class TestPart1(unittest.TestCase):

  def test_isalpha(self):
    self.assertEqual(part1.isalpha(123), 255)
    self.assertEqual(part1.isalpha([1, 2, 3]), 255)

  def test_isdigit(self):
    self.assertEqual(part1.isdigit(123), 255)
    self.assertEqual(part1.isdigit([1,2,3]), 255)

  def test_isalnum(self):
    self.assertEqual(part1.isalnum(124), 255)
    self.assertEqual(part1.isalnum(124.2), 255)

  def test_lencmp(self):
    self.assertEqual(part1.lencmp(123, "def"), 255)
    self.assertEqual(part1.lencmp("def", 123), 255)

  def test_tolower(self):
    self.assertEqual(part1.tolower(123), 255)
    self.assertEqual(part1.tolower(3213.231), 255)

  def test_strcmp(self):
    self.assertEqual(part1.strcmp(123, "abc"), 255)
    self.assertEqual(part1.strcmp("abc", [1,2,3]), 255)
