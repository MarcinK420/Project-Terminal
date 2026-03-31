import shlex
import subprocess

running_commands = {}
running_commands_last_index = 0

def starting(command):
    global running_commands_last_index
    cmd = shlex.split(command)
    cmd = cmd[:-1]
    process = subprocess.Popen(cmd)
    running_commands[running_commands_last_index] = process.pid
    running_commands_last_index += 1
    for index, pid in running_commands.items():
        print(f"[{index}] {pid}")
