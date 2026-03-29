import shlex

def history(command,user_history):
    commands = shlex.split(command)
    if len(commands) > 1 and commands[1].isdigit():
        num_commands = int(commands[1])
        for index, command in enumerate(user_history[-num_commands:], start=len(user_history) - num_commands + 1):
            print(f"{index} {command}")
    elif len(commands) > 1 and commands[1] == '-r':
        path_to_file = commands[2]
        user_history.clear()
        user_history.append(f"history -r {path_to_file}")
        try:
            with open(path_to_file, 'r') as file:
                for line in file:
                    user_history.append(line.strip())
        except FileNotFoundError:
            print(f"File '{path_to_file}' not found.")
    else:
        for index, command in enumerate(user_history, start=1):
            print(f"{index} {command}")