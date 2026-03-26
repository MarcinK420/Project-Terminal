import shlex
import subprocess
from app import quoting


built_ins = ['echo', 'exit', 'type', 'pwd']

def pipeline(command):
    commands = command.split('|')
    left_command = shlex.split(commands[0])
    right_command = shlex.split(commands[1])

    if left_command[0] == 'echo':
        builtin_output = quoting.echo(commands[0]) + '\n'
        p2 = subprocess.Popen(right_command, stdin=subprocess.PIPE, text=True)
        p2.communicate(input=builtin_output)
    elif right_command[0] == 'type':
        p1 = subprocess.Popen(left_command, stdout=subprocess.PIPE)
        p1.communicate()
        from app import main
        print(main.type(commands[1].strip()))

    else:
        p1 = subprocess.Popen(left_command, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(right_command, stdin= p1.stdout)
        p1.stdout.close()
        p2.communicate()

    
    