import unittest
from part1 import *


class TestPart1(unittest.TestCase):

  def test_isalpha(self):
    self.assertEqual(isalpha(123), 255)
    self.assertEqual(isalpha([1, 2, 3]), 255)
    self.assertEqual(isalpha(["a", "b"]), 255)

  def test_isdigit(self):
    self.assertEqual(isdigit(123), 255)
    self.assertEqual(isdigit([1,2,3]), 255)
    self.assertEqual(isdigit(["a", "b"]), 255)

  def test_isalnum(self):
    self.assertEqual(isalnum(124), 255)
    self.assertEqual(isalnum([1, 2, 4]), 255)
    self.assertEqual(isalnum(["a", "b"]), 255)

  def test_lencmp(self):
    self.assertEqual(lencmp(123, "def"), 255)
    self.assertEqual(lencmp("def", 123), 255)
    self.assertEqual(lencmp(["d", "ef"], ""), 255)

  def test_tolower(self):
    self.assertEqual(tolower(123), 255)
    self.assertEqual(tolower(["1","2","3"]), 255)

  def test_strcmp(self):
    self.assertEqual(strcmp(123, "abc"), 255)
    self.assertEqual(strcmp("abc", [1,2,3]), 255)
    self.assertEqual(strcmp("abcd", ["1", "b"]), 255)
