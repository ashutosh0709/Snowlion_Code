import os
import time
import subprocess
import sys

# from subprocess import Popen, CREATE_NEW_CONSOLE

# Popen('cmd', creationflags=CREATE_NEW_CONSOLE)
# input('Enter to exit from Python script...')

from subprocess import *
c = 'jupyter-notebook' #Windows
handle = Popen(c, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
print(handle.stdout.read())
#handle.flush()