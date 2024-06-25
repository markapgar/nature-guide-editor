from ._anvil_designer import GuideListTemplate
from anvil import *
import anvil.server
from ...input_box import InputBox, alert_box, input_box, multi_select_dropdown


class GuideList(GuideListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def new_guide_button_click(self, **event_args):
    results = input_box(title='', items=[{'prompt': 'Title:', 'text': ''}], buttons=['OK', 'Cancel'])
    if results['clicked_button'] == 'OK':
      title = results['Title:']
      ok, msg, id = anvil.server.call('add_guide', title)
      if not ok:
        alert_box(msg)
        return

