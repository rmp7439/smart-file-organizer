# Smart File Organizer

A Python CLI tool that automatically organizes files by extension, detects duplicates, and logs all operations.

## Features
- Organizes files into folders by extension (PDF, MP3, JPG, etc.)
- Detects duplicate files using MD5 hashing
- Logs all operations with timestamps
- Simple CLI interface

## Usage
```bash
# Organize a folder
python3 organizer.py --path /path/to/folder

# Scan for duplicates only
python3 organizer.py --path /path/to/folder --scan
```

## Tech Stack
Python | os | shutil | hashlib | argparse | logging