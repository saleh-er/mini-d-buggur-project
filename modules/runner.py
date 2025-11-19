import subprocess
import json

def run_script(script_path):
    # Charge la config
    with open("config.json", "r") as f:
        config = json.load(f)

    venv_python = config["venv_path"] + "/Scripts/python.exe"

    result = subprocess.run(
        [venv_python, script_path],
        capture_output=True,
        text=True
    )

    return result.stdout, result.stderr
