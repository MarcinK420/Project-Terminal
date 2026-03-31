import shlex
import subprocess

running_commands = {}
running_commands_last_index = 1

def starting(command):
    global running_commands_last_index

    if command.strip().endswith('&'):
        command = command.strip()[:-1].strip()
    cmd = shlex.split(command)
    try:
        process = subprocess.Popen(cmd)
        running_commands[running_commands_last_index] = process.pid
        running_commands_last_index += 1
        for index, pid in running_commands.items():
            print(f"[{index}] {pid}")
    except Exception as e:
        print(f"Error starting command '{command}': {e}")
