from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.server
from ..input_box import InputBox


class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def new_guide_button_click(self, **event_args):
    #title = 
    #ok, msg, id = anvil.server.call('add_guide', title)
    # save_clicked = alert(
    #   content=InputBox(),
    #   title="Add Article",
    #   buttons=[("Save", True), ("Cancel", False)],
    # ) 
    items = [{'prompt': 'Width:', 'text': 10}, {'prompt': 'Height:', 'text': 20}]
    ib = InputBox('Simple input box with items', items=items)
    ib.show()
    self.show_results(ib.results)
    