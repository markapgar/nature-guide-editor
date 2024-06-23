import unittest
from NatureGuides.Guide import *

class GuideTests(unittest.TestCase):
  def test_add_guide(self):
    ok, msg, id = add_guide('Test Guide')
    self.assertTrue(ok, 'basic add did not work')

  def test_empty(self):
    test_fail_msg = 'do not allow empty title'
    ok, msg, id = add_guide(None)
    self.assertFalse(ok, test_fail_msg)
    ok, msg, id = add_guide('')
    self.assertFalse(ok, test_fail_msg)
    ok, msg, id = add_guide(' ')
    self.assertFalse(ok, test_fail_msg)
    self.assertIsNone(id)