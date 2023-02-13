#! /usr/bin/env python3

from pathlib import Path

def main():
    p = Path.home() / "Desktop"
    listfichr(p, "homework")

def print_dir(p, nom):
    for x in p.iterdir():
        if x.is_dir(): 
            print_dir(x)
        elif x.name == nom: 
            print(x)

def listfichNomC(p, nom):
    for x in p.glob("**/" + nom):
        print(x)

def listfichNomS(p, nom):
    for x in p.glob("**/" + nom + ".*"):
        print(x)

def listfich(p=Path.cwd(), s=""):
    for x in p.glob(s + "*"):
        if x.is_file():
            print(x)

def listfichr(p=Path.cwd(), s=""):
    for x in p.glob("**/" + s + "*"):
        print(x)

if __name__ == "__main__":
    main()