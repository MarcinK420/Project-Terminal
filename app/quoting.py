import shlex

def echo(command):
    x = shlex.split(command)
    return " ".join(x[1:])

