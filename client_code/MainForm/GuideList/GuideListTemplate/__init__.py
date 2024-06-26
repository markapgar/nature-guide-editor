from ._anvil_designer import GuideListTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class GuideListTemplate(GuideListTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_button_click(self, **event_args):
    alert(self.item['title'] + self.item['_id'])
