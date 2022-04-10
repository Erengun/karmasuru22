from asyncio import subprocess
import sys
import os
import subprocess

def run_program(folder, name):
    # Exe doesn't work well when we are not cd'ed into it's directory
    os.chdir(folder)
    executable_path = os.path.abspath(name)

    print(f"Executing {executable_path}")
    subprocess.Popen([executable_path])
