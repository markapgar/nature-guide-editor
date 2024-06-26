
class PersistNatureGuidesTest():
  def __init__(self):
    self.guide = {'_id': '[1,1]', 'title': 'default guide'}

  def add_guide(self, title):
    new_id = '[1,2]'
    self.guide = {'_id': '[1,2]', 'title': title}
    return new_id
  
  def find_id_for_title(self, title):
    if self.guide['title'].lower() == title.lower():
      return self.guide['_id']
    return None
  
  def list_guides(self):
    return [self.guide]
