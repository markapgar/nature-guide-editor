import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class PersistNatureGuidesOrm():
  def __init__(self):
    pass

  def search_to_dict(self, search_iterator):
    results = []
    for row in search_iterator:
      results.append(self.row_to_dict(row))
    return results

  def row_to_dict(self, row):
    if row is None:
      return None
      
    d = dict(row)
    d['_id'] = row.get_id()
    return d
  
  # def get_roles(self):
  #   return self.search_to_dict(app_tables.workflow_roles.search())
  
  # def add_role(self, name):
  #   app_tables.workflow_roles.add_row(name=name)
  #   return True, ''

  # def get_role_by_name(self, name):
  #   return self.row_to_dict(app_tables.workflow_roles.get(name=q.ilike(name)))