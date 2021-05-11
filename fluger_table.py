from pandastable import Table, TableModel
from tkinter import Tk, RIGHT, BOTH, RAISED, Menu

class FlugerTable(Table):
    """Custom table class inherits from Table. You can then override required methods"""
    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        self.popupmenu = Menu()

    def handle_left_click(self, event):
        """Example - override left click"""
        Table.handle_left_click(self, event)

    def popupMenu(self, event, rows=None, cols=None, outside=None):
        """Custom right click menu"""
        self.popupmenu = Menu(self, tearoff = 0)

    def popupFocusOut(self, event):
        self.popupmenu.unpost()
        # self.app is a reference to the parent app
        self.popupmenu.add_command(label='do stuff', command=self.app.stuff)
        self.popupmenu.bind("<FocusOut>", self.popupFocusOut)
        self.popupmenu.focus_set()
        self.popupmenu.post(event.x_root, event.y_root)
        return self.popupmenu