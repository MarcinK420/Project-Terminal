import shlex
import subprocess

def redirect_stdout(command):
    x = shlex.split(command)
    for i, word in enumerate(x):
         if word in ('>', '1>'):
              redirect_index = i
              break
    
    komenda = x[:redirect_index]
    filename = x[redirect_index + 1]
    output = None
    if x[0] == 'echo':
        output = " ".join(komenda[1:]) + '\n'
    
    elif x[0] == 'cat':
        try:
             result = subprocess.run(['cat'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
        except Exception:
             output = ''

    elif x[0] == 'ls':
        try:
             result = subprocess.run(['ls'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
        except Exception:
             output = ''
    
    if output is not None:
        with open(filename, "w") as f:
                f.write(output)