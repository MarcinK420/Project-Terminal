import sys
import os

def type(command):
    built_in_commands = ['echo', 'exit', 'type']
    if command[5:] in built_in_commands:
        return f"{command[5:]} is a shell builtin" 
    else:
        system_path = os.environ.get('PATH', '')
        for folder in system_path.split(os.pathsep):
            full_path = os.path.join(folder, command[5:])
            if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                return f"{command[5:]} is {full_path}"
    return f"{command[5:]}: not found"    

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit':
            break
        elif command[:4] == 'echo':
            print(command[5:])
        elif command[:4] == 'type':
            print(type(command))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
