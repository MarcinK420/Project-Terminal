import shlex
import subprocess

def pipeline(command):
    commands = command.split('|')
    left_command = shlex.split(commands[0])
    right_command = shlex.split(commands[1])

    p1 = subprocess.Popen(left_command, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(right_command, stdin= p1.stdout)
    p1.stdout.close()
    p2.communicate()

    
    