import sys
import os
import subprocess
from app import navigation
# import navigation

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
    result = command.split()
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
        elif command == 'pwd':
            print(navigation.print_working_directory())
        elif command[:4] == 'echo':
            print(command[5:])
        elif command[:4] == 'type':
            print(type(command))
        elif executable(command):
            output = executable(command)
            sys.stdout.write(output)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
