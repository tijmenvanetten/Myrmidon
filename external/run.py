# Instantiates all the bots listed in the external/ folder
# and enables their API on a unique port on the localhost

from pathlib import Path
import subprocess

BASE_PORT = 5006
BASE_DIR = Path(__file__).parent

for child in BASE_DIR.glob('*/'):
    if child.is_dir():
        print(f"Starting {child.name}...")
        command = f'cd {child}/ & rasa run --model {child / "models/"} -p {BASE_PORT} --enable-api;'
        subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        BASE_PORT += 1