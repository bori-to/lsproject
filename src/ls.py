import os
import sys

def custom_ls():
    files = os.listdir()

    output = ""
    for file in files:
        if "--rev" in sys.argv:
            output += file[::-1] + "\n"
        else:
            output += file + "\n"

    return output.strip()

if __name__ == '__main__':
    if "-h" in sys.argv:
        print("Usage: python ls.py [--rev]")
    custom_ls()
