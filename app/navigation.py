from pathlib import Path
import os

def print_working_directory():
    return Path.cwd()

def change_working_directory(command):
    if os.path.exists(command):
        os.chdir(command)
        return True
    elif command == '~':
        os.chdir(os.home_dir())
        return True
    else:
        return False

