#! /usr/local/bin/python3

"""
Script to backup all Python related files from Ubuntu VM. Script will make a 
copy of the existing backup with a '.old' extension.
Repository: /Users/ross/Python/UbuntuPythonBackup/
"""

import os
from pathlib import Path
from time import sleep

def folderBackup(BACKUP_DIR):
    """Check for existing directory. If found, add '.old' extension"""
    filepath = Path(BACKUP_DIR)
    if filepath.exists():
        os.system(f"rm -rf {BACKUP_DIR}.old")
        os.system(f"mv {BACKUP_DIR} {BACKUP_DIR}.old")
    else:
        pass

def scp(SOURCE_ADDR, SOURCE_DIR, BACKUP_DIR):
    os.system(f"scp -r {SOURCE_ADDR}:{SOURCE_DIR} {BACKUP_DIR}")

if __name__ == "__main__":
    SOURCE_ADDR = "ross@172.16.210.129"
    SOURCE_DIR = "/home/ross/AllThingsPython/"
    BACKUP_DIR = "/Users/ross/Python/UbuntuPythonBackup"

    folderBackup(BACKUP_DIR)
    scp(SOURCE_ADDR, SOURCE_DIR, BACKUP_DIR)
