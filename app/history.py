import shlex

def history(command,user_history):
    commands = shlex.split(command)
    if commands[1].isdigit():
        num_commands = int(commands[1])
        for index, command in enumerate(user_history[-num_commands:], start=len(user_history) - num_commands + 1):
            print(f"{index} {command}")
    else:
        for index, command in enumerate(user_history, start=1):
            print(f"{index} {command}")