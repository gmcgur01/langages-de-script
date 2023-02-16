#! /usr/bin/env python3

from pathlib import Path

def main():
    rangement(Path.cwd())

def rangement(p):
    
    a = [p/"ARCHIVE/F1K", p/"ARCHIVE/F1M", p/"ARCHIVE/F100M", p/"ARCHIVE/Fsup"]

    for archive in a:
        archive.mkdir(exist_ok = True)

    for x in p.rglob("*"):
        if x.is_file():
            size = x.stat().st_size
            if size < 1024:
                x.rename(a[0] / x.name)
            elif size < 1048576:
                x.rename(a[1] / x.name)
            elif size < 104857600:
                x.rename(a[2] / x.name)
            else:
                x.rename(a[3] / x.name)

    

if __name__ == "__main__":
    main()