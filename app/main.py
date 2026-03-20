import sys
import os
import subprocess
from app import navigation
from app import quoting
from app import redirection
import shlex


def check_path(variable):
        system_path = os.environ.get('PATH', '')
        for folder in system_path.split(os.pathsep):
            full_path = os.path.join(folder, variable)
            if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                return full_path
        
        return None

def type(command):
    built_in_commands = ['echo', 'exit', 'type', 'pwd']
    if command[5:] in built_in_commands:
        return f"{command[5:]} is a shell builtin" 
    else:
        if check_path(command[5:]):
            return f"{command[5:]} is {check_path(command[5:])}"
    return f"{command[5:]}: not found" 

def executable(command):
    # result = command.split()
    result = shlex.split(command)
    filename = result[0]
    if check_path(filename):
        exe_path = check_path(filename)
        output = subprocess.run([filename] + result[1:], executable=exe_path, capture_output=True, text=True)
        return output.stdout
    return None


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit':
            break
        elif '2>' in command:
            redirection.redirect_stderr(command)
        elif '>' in command or '1>' in command:
            redirection.redirect_stdout(command)
        elif '>>' in command or '1>>' in command:
            redirection.append_stdout(command)       
        elif command[:2] == 'cd':
            if navigation.change_working_directory(command[3:]):
                pass
            else:
                print(f"cd: {(command[3:])}: No such file or directory")
        elif command == 'pwd':
            print(navigation.print_working_directory())
        elif command[:4] == 'echo':
            print(quoting.echo(command))
        elif command[:4] == 'type':
            print(type(command))
        elif command[:3] == 'cat':
            quoting.cat(command)
        elif executable(command):
            output = executable(command)
            sys.stdout.write(output)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
