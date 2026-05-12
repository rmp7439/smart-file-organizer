import os
import shutil

def get_files(target):
    files = []
    for f in os.listdir(target):
        if os.path.isfile(os.path.join(target, f)):
            files.append(f)
    return files

def get_extension(filename):
    name, ext = os.path.splitext(filename)
    return ext.lower() if ext else ".unknown"

def organize_files(target):
    files = get_files(target)
    for f in files:
        ext = get_extension(f)
        folder_name = ext[1:].upper() if ext != ".unknown" else "UNKNOWN"
        dest = os.path.join(target, folder_name)
        os.makedirs(dest, exist_ok=True)
        src = os.path.join(target, f)
        dst = os.path.join(dest, f)
        shutil.move(src, dst)
        print(f"Moved {f} -> {folder_name}/")

organize_files(".")
