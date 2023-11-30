#!/usr/bin/python3
import os
import sys

def custom_ls():
    files = os.listdir()

    for file in files:
        if "--rev" in sys.argv:
            print(file[::-1])
        else :
            print(file)

if __name__ == '__main__':
    if "-h" in sys.argv:
        print("Usage: python ls.py [--rev]")
    custom_ls()
