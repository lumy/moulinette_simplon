import os
import unittest
import inspect
import sys
import subprocess

class TestCheckPassword(unittest.TestCase):
  def tearDown(self):
    try:
      os.remove("mydb.db")
    except:
      pass


  def _com(self, *my_cmd):
    folder_content = os.listdir(os.path.join(sys.path[0], "part4"))
    if "mydb.py" in folder_content:
      cmd = os.path.join(os.path.join(sys.path[0], "part4"), "mydb.py")
      proc = subprocess.run(["/usr/bin/python", cmd, *my_cmd], capture_output=True)
      return proc
    return None

  def test_bonus(self):
    pass

  def test_checkpwd(self):
    proc = self._com("get", "lumy")
    self.assertEqual(proc.stdout, b'')
    proc = self._com("add", "lumy", "yep")
    self.assertEqual(proc.stdout, b'')
    proc = self._com("get", "lumy")
    self.assertEqual(proc.stdout.strip(), b'yep')
    proc = self._com("add", "lumy", "stop")
    self.assertEqual(proc.stdout, b'')
    proc = self._com("add", "monday", "test")
    self.assertEqual(proc.stdout, b'')
    proc = self._com("get", "lumy")
    self.assertEqual(proc.stdout.strip(), b'stop')
    proc = self._com("get", "monday")
    self.assertEqual(proc.stdout.strip(), b'test')
