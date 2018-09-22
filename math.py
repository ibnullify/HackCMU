import pexpect, re, time

### Just for the shell
import tkinter as tk
from GUITools import InterpreterText as shell

### Create a Mathematica instance bound to a controlled kernel

wolfker="/Applications/Mathematica.app/Contents/MacOS/WolframKernel"
proc=pexpect.spawn(wolfker)
script='https://raw.githubusercontent.com/b3m2a1/mathematica-tools/master/SubprocessKernel.wl'
cmd='Get["{}"]; SubprocessKernel`OpenSubprocessNotebook[];'.format(script)
proc.sendline(cmd)
proc.expect('Starting kernel\.\.\.')

### Convenience function for getting junk out of Mathematica

def call_mathematica(cmd):
    proc.expect(".*")
    proc.sendline(cmd)
    proc.expect(r"(>> ------ Output: \d+ ------ >>)|(Out\[)")
    leader=proc.after.decode()
    if leader.startswith('>> ------ Output:'):
        proc.expect('<< ------ Output: \d+ ------ <<')
        leader=leader+proc.before.decode()+proc.after.decode()
    proc.expect(".+")
    res=leader+proc.after.decode()
    chunks=re.findall(r'>> ------ Output: \d+ ------ >>.*?<< ------ Output: \d+ ------ <<', res, re.DOTALL)

    if len(chunks)==0:
        chunks=res
    else:
        chunks=["\n".join(chunk.splitlines()[1:-2]) for chunk in chunks]

    if len(chunks)==1:
        chunks=chunks[0]

    return chunks

### Create a little shell to interact with the made Mathematica instance

mathshell=shell(variables={'Mathematica':proc, 'call_mathematica':call_mathematica});
mathshell.pack(expand=True, fill='both');
mathshell.mainloop()
