import os


def list_files(path):
    for file in os.listdir(path):
        print(file)


list_files(".")
