# AdobeBlocker/widgets.py

import tkinter as tk
from tkinter import ttk
from AdobeBlocker import utils

class BlockToggleButton(ttk.Button):
    """
    A custom ttk Button that toggles between Block/Unblock
    based on the current state of the hosts file.
    The button displays red text and outline when in "Block" state,
    and green when in "Unblock" state.
    """
    def __init__(self, parent, **kwargs):
        # Initialize styles
        self.style = ttk.Style()
        # "Block" style: red text and outline
        self.style.configure("Block.TButton", foreground="red", borderwidth=2)
        # "Unblock" style: green text and outline
        self.style.configure("Unblock.TButton", foreground="green", borderwidth=2)
        
        super().__init__(parent, command=self._on_click, **kwargs)
        self._update_text()

    def _on_click(self):
        if utils.is_blocked():
            utils.unblock()
        else:
            utils.block()
        self._update_text()

    def _update_text(self):
        if utils.is_blocked():
            # Hosts file is blocked so button toggles to Unblock with green style.
            self.config(text="Unblock", style="Unblock.TButton")
        else:
            # Hosts file is unblocked so button toggles to Block with red style.
            self.config(text="Block", style="Block.TButton")
