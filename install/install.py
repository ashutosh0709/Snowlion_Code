
# This script is responsible for automated installation of nessesary libraries and creation of environment for the main code to run in.

############################################################################################################################

import os
import subprocess
import sys
import time
import threading
from subprocess import Popen, CREATE_NEW_CONSOLE

############################################################################################################################
# Validating Python Version:

try:
    output = subprocess.run(["python" , "--version"], stdout=subprocess.PIPE, text=True)
except:
    try:
        output = subprocess.run(["python3" , "--version"], stdout=subprocess.PIPE, text=True)
    except:
        sys.exit("Installation UNSUCCESSFULL!!! Please Contact Developer!")     

python_version = str(output.stdout)
i = len(python_version)-1
while python_version[i] != '.':
    i -= 1

python_version = python_version[0:i]
python_version = python_version.split(' ')[-1]
python_version = float(python_version)

version_error_msg = 'Python Version 3.6 - 3.9 is required, but you have : Python-' + str(python_version) + '\nPlease Reinstall Python in this version range, 3.8.10 is recommended\nPLEASE TRY AGAIN!'
if python_version < 3.6 or python_version > 3.9:
    sys.exit(version_error_msg)
else:
    print('Python version -> Compatible')

print('Please wait for necessary Libraries to be installed and Virtual Environment to be created for the code to run in.')

#############################################################################################################################
# Creating and setting up the virtual Environment:

from venv import create
from os.path import join, expanduser
from subprocess import run
from os.path import abspath

activate_this_file = "./../venv/Scripts/activate_this.py"
exec(compile(open(activate_this_file, "rb").read(), activate_this_file, 'exec'), dict(__file__=activate_this_file))
run(["pip", "install", "-r", abspath(".\\install\\requirements.txt")], cwd=dir)

#############################################################################################################################

print("\n\n\n\n\n\nSuccessfully Installed!!!")