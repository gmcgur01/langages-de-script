#! /usr/bin/env python3

from pathlib import Path

def main():
    recent_files()

def recent_files(p=Path.cwd()):
    files = [x for x in p.glob("*") if x.is_file()]
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    for file in files[:10]:
        print(file)

def recent_files_r(p=Path.cwd()):
    files = [x for x in p.glob("**/*") if x.is_file()]
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    for file in files[:10]:
        print(file)

if __name__ == "__main__":
    main()