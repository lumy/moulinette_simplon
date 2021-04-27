import unittest
import inspect
import sys
from part3 import cpwd

class TestCheckPassword(unittest.TestCase):
  def tearDown(self):
    """Should be implemented in every Test easier than doing it in unload_context"""
    try:
      del sys.modules['part3.cpwd']
    except:
      pass
    try:
      del sys.modules['part3']
    except:
      pass
    return super(TestCheckPassword, self).tearDown()


  def test_bonus(self):
    self.assertTrue(cpwd.check_password(b"test", "a71079d42853dea26e453004338670a53814b78137ffbed07603a41d76a483aa9bc33b582f77d30a65e6f29a896c0411f38312e1d66e0bf16386c86a89bea572", "blake"))
    self.assertTrue(cpwd.check_password(b"Home Coming", "a958c127358721fb0bb684764dc3516a4de3ad77da0614d277a3d9d5c94d7d0f62a46df5990b739d374be153c6cb520d415ddb0271e3c6e614070de6de2bcb76", "blake"))

  def test_checkpwd(self):
    self.assertTrue(cpwd.check_password(b"test", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"))
    self.assertTrue(cpwd.check_password(b"Home Coming", "324289aa805c03234ee8b518523ba726256939e87b4f147a4b4ec1f2372a36cc"))
