# AdobeBlocker/config.py
import sys
import os

def resource_path(relative_path: str) -> str:
    """Get absolute path to a resource, works for dev and PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Absolute path to the Windows hosts file remains unchanged.
HOSTS_FILE_PATH = r"C:\Windows\System32\drivers\etc\hosts"

# Local fallback block list path bundled inside the exe
BLOCK_LIST_PATH = resource_path(os.path.join("data", "adobe_block_list.txt"))

# Icon path for the main window and taskbar
ICON_PATH = resource_path(os.path.join("img", "AdobeBlocker.ico"))
