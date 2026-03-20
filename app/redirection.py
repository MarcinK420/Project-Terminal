import shlex
import subprocess
import sys

def redirect_stdout(command):
    x = shlex.split(command)
    redirect_index = None
    output = None
    for i, word in enumerate(x):
         if word in ('>', '1>'):
              redirect_index = i
              break
    
    if redirect_index is None:
         return
    
    komenda = x[:redirect_index]
    filename = x[redirect_index + 1]
    output = None
    if x[0] == 'echo':
        output = " ".join(komenda[1:]) + '\n'
    
    elif x[0] == 'cat':
        try:
             result = subprocess.run(['cat'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
             if result.stderr:
                  sys.stderr.write(result.stderr)
        except Exception as e:
             sys.stderr.write(f"cat: {e}\n")

    elif x[0] == 'ls':
        try:
             result = subprocess.run(['ls'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
             if result.stderr:
                  sys.stderr.write(result.stderr)
        except Exception as e:
             sys.stderr.write(f"ls: {e}\n")
    
    if output is not None:
        with open(filename, "w") as f:
                f.write(output)

def append_stdout(command):
    x = shlex.split(command)
    redirect_index = None
    output = None
    for i, word in enumerate(x):
         if word in ('>', '1>'):
              redirect_index = i
              break
    
    if redirect_index is None:
         return
    
    komenda = x[:redirect_index]
    filename = x[redirect_index + 1]
    output = None
    if x[0] == 'echo':
        output = " ".join(komenda[1:]) + '\n'
    
    elif x[0] == 'cat':
        try:
             result = subprocess.run(['cat'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
             if result.stderr:
                  sys.stderr.write(result.stderr)
        except Exception as e:
             sys.stderr.write(f"cat: {e}\n")

    elif x[0] == 'ls':
        try:
             result = subprocess.run(['ls'] + komenda[1:], capture_output=True, text=True)
             output = result.stdout
             if result.stderr:
                  sys.stderr.write(result.stderr)
        except Exception as e:
             sys.stderr.write(f"ls: {e}\n")
    
    if output is not None:
        with open(filename, "a") as f:
                f.write(output + '\n')

def redirect_stderr(command):
    x = shlex.split(command)
    redirect_index = None
    output = None
    for i, word in enumerate(x):
         if word == '2>':
              redirect_index = i
              break
    if redirect_index is None:
         return 
    komenda = x[:redirect_index]
    filename = x[redirect_index + 1]    
    if x[0] == 'echo':
        sys.stdout.write(" ".join(komenda[1:]) + '\n')
        output = ''

    elif x[0] == 'cat':
        try:
             result = subprocess.run(['cat'] + komenda[1:], capture_output=True, text=True)
             sys.stdout.write(result.stdout)
             output = result.stderr
        except Exception as e:
             output = f"cat: {e}\n"

    elif x[0] == 'ls':
        try:
             result = subprocess.run(['ls'] + komenda[1:], capture_output=True, text=True)
             sys.stdout.write(result.stdout)
             output = result.stderr
        except Exception as e:
             output = f"ls: {e}\n"   

    if output is not None:
        with open(filename, "w") as f:
                f.write(output)
    