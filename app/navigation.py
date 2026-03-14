from pathlib import Path
import os

def print_working_directory():
    return Path.cwd()

def change_working_directory(command):
    if os.path.exists(command):
        return os.chdir(command)
    else:
        return None

