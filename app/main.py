import sys

def type(command):
    built_in_commands = ['echo', 'exit', 'type']
    if command[5:] in built_in_commands:
        return f"{command[5:]} is a shell builtin" 
    else:
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
