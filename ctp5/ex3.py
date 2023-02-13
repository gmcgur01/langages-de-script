#! /usr/bin/env python3

from pathlib import Path

def main():
    listfichNiv(Path.home() / "Desktop", ".pdf")

def listfichNiv(p=Path.cdw(), suf=""):
    for x in p.glob("**/*"):
        if x.suffix == suf and len(x.parents) > 2:
            print(x) 

if __name__ == "__main__":
    main()