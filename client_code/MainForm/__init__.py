from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..input_box import InputBox, alert_box, input_box, multi_select_dropdown
from .GuideInfoForm import GuideInfoForm
from .GuideList import GuideList


class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def show_guides_buttton_click(self, **event_args):
    g = GuideList()
    self.content_panel.add_component(g)
    pass

  def show_guide(self, id):
    self.content_panel.clear()
    g = GuideInfoForm()
    g.guide_id = id
    self.content_panel.add_component(g)
        
    