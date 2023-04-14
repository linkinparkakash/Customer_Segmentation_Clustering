import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the project name: ")
    if project_name !='':
        break

logging.info(f"Creating Project: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/ci.yaml",
    f"src/{project_name}/__init__.py",
    f"test/__init__.py",
    f"configs/config.yaml",
    f"docs/index.md",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "main.py",
    "mkdocs.yaml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new file directory at : {filedir} for the path: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"File already exists at: {filepath}")