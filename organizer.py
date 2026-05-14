import os
import shutil
import hashlib
import argparse

def get_files(target):
    files = []
    for f in os.listdir(target):
        full_path = os.path.join(target, f)
        if os.path.isfile(full_path) and f != "organizer.py":
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

def get_file_hash(filepath):
    try:
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing {filepath}: {e}")
        return None

def find_duplicates(target):
    hashes = {}
    duplicates = []
    files = get_files(target)
    for f in files:
        filepath = os.path.join(target, f)
        file_hash = get_file_hash(filepath)
        if file_hash is None:
            continue
        if file_hash in hashes:
            duplicates.append((f, hashes[file_hash]))
        else:
            hashes[file_hash] = f
    return duplicates

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("--path", type=str, default=".", help="Path to folder to organize")
    parser.add_argument("--scan", action="store_true", help="Scan for duplicates only")
    args = parser.parse_args()

    print(f"Scanning {args.path} for duplicates...")
    dupes = find_duplicates(args.path)
    if dupes:
        for dupe, original in dupes:
            print(f"Duplicate found: {dupe} is a copy of {original}")
    else:
        print("No duplicates found.")

    if not args.scan:
        organize_files(args.path)