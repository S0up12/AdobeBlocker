# AdobeBlocker/utils.py

import os
import requests
from AdobeBlocker import config

# URL to the online block list (update with your actual GitHub raw URL)
BLOCK_LIST_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/Adobe_Block_List.txt"

def read_block_list() -> list[str]:
    """
    Fetch block list lines from the online URL.
    If the online fetch fails, fallback to reading the local file.
    """
    try:
        response = requests.get(BLOCK_LIST_URL, timeout=5)
        response.raise_for_status()  # Raise an error if the request failed
        block_list = [line.strip() for line in response.text.splitlines() if line.strip()]
        return block_list
    except Exception as e:
        print("Online block list fetch failed, falling back to local file.", e)
        lines = []
        try:
            with open(config.BLOCK_LIST_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        lines.append(line)
        except FileNotFoundError:
            print("Local block list file not found.")
        return lines

def is_blocked() -> bool:
    """
    Check if all lines from the block list (online or fallback) appear in the hosts file.
    """
    block_lines = read_block_list()
    try:
        with open(config.HOSTS_FILE_PATH, "r", encoding="utf-8") as f:
            hosts_lines = [l.strip() for l in f if l.strip()]
        return all(line in hosts_lines for line in block_lines)
    except FileNotFoundError:
        # If the hosts file doesn't exist for some reason, treat as unblocked
        return False

def block():
    """
    Append block lines to the hosts file if they aren't already there.
    """
    block_lines = read_block_list()
    try:
        with open(config.HOSTS_FILE_PATH, "r", encoding="utf-8") as f:
            existing_lines = [l.strip() for l in f]

        with open(config.HOSTS_FILE_PATH, "a", encoding="utf-8") as f:
            for line in block_lines:
                if line not in existing_lines:
                    f.write("\n" + line)
    except FileNotFoundError:
        print("Hosts file not found.")

def unblock():
    """
    Remove the block lines from the hosts file if present.
    """
    block_lines = read_block_list()
    try:
        with open(config.HOSTS_FILE_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Filter out any lines that match the block lines
        new_lines = [line for line in lines if line.strip() not in block_lines]

        with open(config.HOSTS_FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    except FileNotFoundError:
        print("Hosts file not found.")
