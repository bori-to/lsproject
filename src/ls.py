import os
import sys

def resolve_symlink(path):
    target = os.path.realpath(path)
    return f"{path} -> {target}"

def custom_ls():
    files = os.listdir()

    output = ""
    for file in files:
        if os.path.islink(file):
            file = resolve_symlink(file)
        if "--rev" in sys.argv:
            output += file[::-1] + "\n"
        else:
            output += file + "\n"

    return output.strip()

if __name__ == '__main__':
    if "-h" in sys.argv:
        print("Usage: python ls.py [--rev]")
        exit()
    print(custom_ls())
