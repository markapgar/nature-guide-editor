import anvil.server
from .Validate import *

@anvil.server.callable()
def add_guide(title):
  if title is None:
    return False, 'Title cannot be blank', None
  if is_blank(title):
    return False, 'Title cannot be blank', None
  return True, '', 1

class Guide():
  def __init__(self, title) -> None:
    self.title = title

  
