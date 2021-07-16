""" 
Instantiates all the bots listed in the external/ folder
and enables their API on a unique port on the localhost
"""

import os
import signal
import subprocess
from pathlib import Path


BASE_PORT = 5006
BASE_DIR = Path(__file__).parent

# Iterate over folders in external/
for child in BASE_DIR.glob('*/'):
    if child.is_dir():
        print(f"Starting {child.name} server...")
        command = f'cd {child}/ & rasa run --model {child / "models/"} -p {BASE_PORT} --enable-api;'
        pro = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        BASE_PORT += 1