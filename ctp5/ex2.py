#! /usr/bin/env python3

from pathlib import Path

def main():
    L = ["Hello", "guys", "it's", "me", "I'm", "gotta", "here"]
    Sauvegarde(L)

def Sauvegarde(L):
    p = Path() / "ARCHIVE"
    p.mkdir(exist_ok=True)
    for i, line in enumerate(L):
        curr_p = p / ("fich_" + str(i) + ".txt")
        curr_p.write_text(line)

if __name__ == "__main__":
    main()