
import anvil

@anvil.server.portable_class
class Guide:
  def __init__(self, title):
    self.title = title
