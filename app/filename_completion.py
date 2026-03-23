import readline
import os

def get_autocompletion():
    commands = ['echo', 'exit', 'type', 'pwd', 'cd', 'cat', 'ls']
    system_path = os.environ.get('PATH', '')

    for folder in system_path.split(os.pathsep):
        if os.path.isdir(folder):
            try:
                for filename in os.listdir(folder):
                    filepath = os.path.join(folder, filename)
                    if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
                        commands.append(filename)
            except PermissionError:
                pass
    
    return list(set(commands))

commands = get_autocompletion()

def completer(text, state):
    line = readline.get_line_buffer()
    words = line.split()

    #Jesli nie ma jescze wpisanych slow lub konczymy dopiero pierwsze slowo
    if len(words) == 0 or (len(words) == 1 and not line.endswith(' ')):
        if state == 0:
            completer.matches = sorted([cmd for cmd in commands if cmd.startswith(text)])
        try:
            match = completer.matches[state]
            if len(completer.matches) == 1:
                return match + ' '
            return match
        except (AttributeError, IndexError):
            return None
        
    #Jesli jestesmy juz po pierwszym slowie i probujemy dokonac podpowiedzi nazwy pliku
    elif len(words) >= 1:
        cmd = words[0]
        filename_commands = ['cat', 'ls', 'cd', 'less', 'vim', 'nano']

        if cmd in filename_commands:
            try:
                current_dir = os.getcwd()

                if '/' in text:
                    last_slash_idx = text.rfind('/')
                    dir_part = text[:last_slash_idx + 1]
                    filename_part = text[last_slash_idx + 1:]

                    search_dir = os.path.join(current_dir, dir_part)
                else:
                    dir_part = ''
                    filename_part = text
                    search_dir = current_dir
                
                if os.path.isdir(search_dir):
                    if state == 0:
                        files = [f for f in os.listdir(search_dir) if f.startswith(filename_part)]
                        completer.matches = sorted([dir_part + f for f in files])
                    
                    try:
                        match = completer.matches[state]
                        return match + ' '
                    except (AttributeError, IndexError):
                        return None
            except (OSError, AttributeError):
                return None