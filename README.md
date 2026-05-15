# Smart File Organizer

A Python CLI tool that automatically organizes files by type, detects duplicates using MD5 hashing, and logs all operations.

## Features

- Organizes files into folders by extension (PDF, MP3, JPG, etc.)
- Detects duplicate files using MD5 hashing
- Logs all operations with timestamps
- Simple CLI interface

## Language

Python 3

## Modules Used

- os
- shutil
- hashlib
- argparse
- logging

## Installation

```bash
git clone https://github.com/rmp7439/smart-file-organizer
cd smart-file-organizer
```

## Usage

```bash
# Organize a folder
python3 organizer.py --path /path/to/folder

# Scan for duplicates only
python3 organizer.py --path /path/to/folder --scan
```

## Project Structure

```text
smart-file-organizer/
├── organizer.py
├── organizer.log
├── .gitignore
└── README.md
```

## Future Improvements

- GUI support
- Undo functionality
- Real-time directory monitoring
- Custom organization rules