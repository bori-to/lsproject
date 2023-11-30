import os

def custom_ls():
    files = os.listdir()

    for file in files:
        print(file)

custom_ls()
