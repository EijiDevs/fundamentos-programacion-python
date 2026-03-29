import os
import subprocess

def clear() -> None:
    if os.name == "posix":
        os.environ.setdefault('TERM', 'xterm-256color')
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)