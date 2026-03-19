import shlex

def echo(command):
    x = shlex.split(command)
    return " ".join(x[1:])

def cat(command):
    x = shlex.split(command)
    filenames = x[1:]
    for name in filenames:
        with open(name, 'r') as file:
            print(file.read())

    return 1

