import shlex

last_appended_index = 0

def history(command,user_history):
    commands = shlex.split(command)
    if len(commands) > 1 and commands[1].isdigit():
        num_commands = int(commands[1])
        for index, command in enumerate(user_history[-num_commands:], start=len(user_history) - num_commands + 1):
            print(f"{index} {command}")
    elif len(commands) > 1 and commands[1] == '-r':
        history_read_file(commands,user_history)
    elif len(commands) > 1 and commands[1] == '-w':
        history_write_file(commands,user_history)
    elif len(commands) > 1 and commands[1] == '-a':
        history_append_file(commands,user_history)
    else:
        for index, command in enumerate(user_history, start=1):
            print(f"{index} {command}")

def history_read_file(commands,user_history):
    path_to_file = commands[2]
    user_history.clear()
    user_history.append(f"history -r {path_to_file}")
    try:
        with open(path_to_file, 'r') as file:
            for line in file:
                user_history.append(line.strip())
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found.")

def history_write_file(commands,user_history):
    path_to_file = commands[2]
    try:
        with open(path_to_file, 'w') as file:
            for command in user_history:
                file.write(command + '\n')
    except Exception as e:
        print(f"Error writing to file '{path_to_file}': {e}")

def history_append_file(commands,user_history):
    path_to_file = commands[2]
    global last_appended_index
    try:
        with open(path_to_file, 'a') as file:
            for command in user_history[last_appended_index:]:
                file.write(command + '\n')
        
        last_appended_index = len(user_history)
                
    except Exception as e:
        print(f"Error appending to file '{path_to_file}': {e}")