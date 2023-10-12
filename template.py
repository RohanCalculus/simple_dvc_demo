# Import libraries
import os

# List of directories to be created
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

# Creating directories with each child folder having .gitkeep file so that it can be pushed to github repo
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

# List of files to be created
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__intit__.py"),
]

# Creating the files
for file_ in files:
    with open(file_, "w") as f:
        pass