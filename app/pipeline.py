import shlex
import subprocess
from app import quoting

built_ins = ['echo', 'exit', 'type', 'pwd']

def pipeline(command):
    commands_text = command.split('|')
    
    prev_process = None
    
    for i, cmd_text in enumerate(commands_text):
        cmd = shlex.split(cmd_text) # Parsujemy np. 'head -n 3' -> ['head', '-n', '3']
        is_last = (i == len(commands_text) - 1)

        if cmd[0] in built_ins:
            out_text = ''

            if cmd[0] == 'echo':
                out_text = quoting.echo(cmd_text) + '\n'
            elif cmd[0] == 'type':
                from app import main
                out_text = main.type(cmd_text.strip()) + '\n'
            
            if prev_process:
                prev_process.communicate()

            if is_last:
                print(out_text, end='')
                current_process = None
            else:
                import os
                r, w = os.pipe()
                os.write(w, out_text.encode())
                os.close(w)

                class DummyProces:
                    def __init__(self, fd):
                        self.stdout = open(fd, 'rb')
                    def communicate(self):
                        pass

                current_process = DummyProces(r)
        
        else:
            if prev_process:
                current_stdin = prev_process.stdout
            else:
                current_stdin = None
                
            if is_last:
                current_stdout = None
            else:
                current_stdout = subprocess.PIPE

            current_process = subprocess.Popen(cmd, stdin=current_stdin, stdout=current_stdout)  # <- Tu musisz uzupełnić!
            
            if prev_process:
                prev_process.stdout.close()

        prev_process = current_process

    if prev_process:
        prev_process.communicate()



    
    