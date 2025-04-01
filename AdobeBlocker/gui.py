# AdobeBlocker/gui.py

import tkinter as tk
from tkinter import ttk
import sv_ttk
from AdobeBlocker import config
from AdobeBlocker.widgets import BlockToggleButton

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Basic window config
        self.title("Adobe Blocker")
        self.minsize(250, 100)  # Set minimum window size

        # Set the window/taskbar icon (Windows)
        self.iconbitmap(config.ICON_PATH)
        
        # Apply Sun-Valley theme (light or dark)
        sv_ttk.use_light_theme()
        # Alternatively, use: sv_ttk.use_dark_theme()

        # Main frame
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Toggle button (bigger with extra padding)
        self.toggle_button = BlockToggleButton(main_frame)
        self.toggle_button.pack(pady=10, ipadx=30, ipady=10)
        
        # Center the window on the screen
        self.update_idletasks()  # Update "requested size" from geometry manager
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")
