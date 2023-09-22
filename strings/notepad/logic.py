import os
import sys


def create_dir():
    os.chdir("/home/user/practice-projects/strings/notepad")
    new_dir = "files"
    # new_dir_path = os.path.join(current_dir, new_dir)
    os.mkdir(new_dir)
    os.chdir("/home/user/practice-projects/strings/notepad")
    return new_dir

def delete_dir():
    pass


def create_new_file(path):
    os.chdir(path)
    with open(f"{path}/newFile.txt") as f:
        pass
    return f"{path}/newFile.txt"


def save_file():
    pass


def open_file():
    pass


def write_to_file():
    pass


def delete_file():
    pass

