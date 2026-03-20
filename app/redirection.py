import shlex

def redirect_stdout(command):
    x = shlex.split(command)
    if x[0] == 'echo':
        i = 1
        output = ''
        while True:
            if x[i] == '>' or x[i] == '1>':
                k = i + 1
                break
            else:
                output = output + x[i] + ' '
                i += 1

        filename = x[k:]
        with open(filename, "w") as f:
            f.write(output)