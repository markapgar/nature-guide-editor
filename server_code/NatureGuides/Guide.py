import anvil.server
from .Validate import *
from .PersistNatureGuides import PersistNatureGuides

import inspect

def set_persist(persist):
  Guide.set_persist(persist)

@anvil.server.callable()
def add_guide(title):
  if title is None:
    return False, 'Title cannot be blank', None
  if is_blank(title):
    return False, 'Title cannot be blank', None
  if Guide.find_id_for_title(title):
    return False, 'Already a guide with that title', None

  return True, '', Guide.add_guide(title)

class Guide():
  persist = PersistNatureGuides()

  def __init__(self) -> None:
    self.title = ''

  @classmethod
  def set_persist(cls, persist):
    cls.persist = persist

  @classmethod
  def find_id_for_title(cls, title):
    return cls.persist.find_id_for_title(title)
  
  @classmethod
  def add_guide(cls, title):
    return cls.persist.add_guide(title)
    
