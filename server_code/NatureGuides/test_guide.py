import unittest
from .Guide import *
from .PersistNatureGuidesTest import PersistNatureGuidesTest

class GuideTests(unittest.TestCase):
  
  def setUp(self):
    set_persist(PersistNatureGuidesTest())

  def test_add_guide(self):
    ok, msg, id = add_guide('Test Guide')
    self.assertTrue(ok, 'basic add did not work')
    self.assertIsNotNone(id)

  def test_empty(self):
    test_fail_msg = 'do not allow empty title'
    ok, msg, id = add_guide(None)
    self.assertFalse(ok, test_fail_msg)
    self.assertIsNone(id, 'return id=None if not ok')
    ok, msg, id = add_guide('')
    self.assertFalse(ok, test_fail_msg)
    ok, msg, id = add_guide(' ')
    self.assertFalse(ok, test_fail_msg)

  def test_duplicates(self):
    set_persist(PersistNatureGuidesTest())
    test_fail_msg = 'do not allow duplicates'
    dup = 'dup_guide'
    ok, msg, id = add_guide(dup)
    self.assertTrue(ok)
    ok, msg, id = add_guide(dup)
    self.assertFalse(ok, test_fail_msg)

    
    # self.assertFalse(ok, test_fail_msg)
