import shlex

def history(command,user_history):
    commands = shlex.split(command)
    if len(commands) > 1 and commands[1].isdigit():
        num_commands = int(commands[1])
        for index, command in enumerate(user_history[-num_commands:], start=len(user_history) - num_commands + 1):
            print(f"{index} {command}")
    elif len(commands) > 1 and user_history[-1] == '-r':
        path_to_file = user_history[-1].split()[-1]
        try:
            with open(path_to_file, 'r') as file:
                for index, line in enumerate(file, start=1):
                    print(f"{index} {line.strip()}")
        except FileNotFoundError:
            print(f"File not found: {path_to_file}")
    else:
        for index, command in enumerate(user_history, start=1):
            print(f"{index} {command}")