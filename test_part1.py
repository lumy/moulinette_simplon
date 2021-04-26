import unittest
from part1 import *


class TestPart1(unittest.TestCase):

    def test_isalpha(self):
        self.assertTrue(isalpha("abc"))
        self.assertFalse(isalpha("ab2c"))
        self.assertTrue(isalpha("ABC"))
        self.assertFalse(isalpha("ABC#"))

    def test_isdigit(self):
        self.assertFalse(isdigit("abc"))
        self.assertFalse(isdigit("abc#"))
        self.assertFalse(isdigit("a2bc"))
        self.assertTrue(isdigit("2567"))

    def test_isalnum(self):
        self.assertFalse(isalnum("abc#"))
        self.assertTrue(isalnum("a2bc"))
        self.assertTrue(isalnum("1234"))

    def test_lencmp(self):
        self.assertEqual(lencmp("abd", "def"), 0)
        self.assertEqual(lencmp("gesfsabd", "def"), 1)
        self.assertEqual(lencmp("def", "gesfsabd"), -1)

    def test_tolower(self):
        self.assertEqual(tolower("ABDE"), "abde")
        self.assertEqual(tolower("AB#23DE"), "ab#23de")
        self.assertEqual(tolower("AbCDEF1234"), "abcdef1234")

    def test_strcmp(self):
        self.assertEqual(strcmp("ABC", "abc"), 0)
        self.assertEqual(strcmp("abc", "abc"), 0)
        self.assertEqual(strcmp("abcd", "abc"), 1)
        self.assertEqual(strcmp("e", "abc"), 1)
        self.assertEqual(strcmp("abcd", "fabc"), -1)
        self.assertEqual(strcmp("abcd", "abcda"), -1)


if __name__ == '__main__':
    unittest.main()
