import os


def create_dir(dir_name):
    os.mkdir(dir_name)
    os.chdir("/home/user/practice-projects/files")
    path_to_dir = os.getcwd()
    return path_to_dir


def delete_dir(path):
    try:
        os.rmdir(path)
        return "Deleted Directory"
    except OSError:
        return "Can not delete directory. \nCan only delete empty directories."


def create_new_file(path):
    os.chdir(path)
    f = open(f"{path}/newFile.txt", "x")
    return f"{path}/newFile.txt"


def save_file():
    pass


def display_file(file_path):
    print(file_path)
    f = open(file_path, "r", encoding="utf-8")
    print(f.read())
    f.close()


def write_to_file(path):
    with open(path, "a", encoding="utf-8") as f:
        str = input("Type: ")
        f.write(str)
    return f.closed


def delete_file(path):
    try:
        os.remove(path)
        return "File Deleted."
    except OSError:
        return "File could nit be deleted."
