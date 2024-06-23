from ._anvil_designer import GuideInfoFormTemplate
from anvil import *
import anvil.server


class GuideInfoForm(GuideInfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    self.refresh_data_bindings()