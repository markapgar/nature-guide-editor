import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class PersistNatureGuides():
  def __init__(self):
    pass

  def row_to_dict(self, row):
    if row is None:
      return None
      
    d = dict(row)
    d['_id'] = row.get_id()
    return d

  def search_to_dict(self, search_iterator):
    results = []
    for row in search_iterator:
      results.append(self.row_to_dict(row))
    return results  
  
  def find_id_for_title(self, title):
    row = app_tables.guides.get(title=q.ilike(title))
    if row is not None:
      return row.get_id()
    return None

  # def find_id_for_title(self, title):
  #   row = app_tables.guides.get(title=q.ilike(title))
  #   if row is not None:
  #     return row.get_id()
  #   return None

  def add_guide(self, title):
    return app_tables.guides.add_row(title=title).get_id()
