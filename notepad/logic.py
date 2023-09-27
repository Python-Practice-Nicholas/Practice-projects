import os
import sys


def create_dir():
    os.chdir("/home/user/practice-projects/strings/notepad")
    new_dir = "files"
    # new_dir_path = os.path.join(current_dir, new_dir)
    os.mkdir(new_dir)
    os.chdir("/home/user/practice-projects/strings/notepad/files")
    return os.getcwd()


def delete_dir():
    pass


def create_new_file(path):
    os.chdir(path)
    f = open(f"{path}/newFile.txt")
    f.close()
    return f"{path}/newFile.txt"


def save_file():
    pass


def open_file():
    pass


def write_to_file():
    pass


def delete_file():
    pass

