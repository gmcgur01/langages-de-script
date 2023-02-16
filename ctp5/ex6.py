#! /usr/bin/env python3

from pathlib import Path
import re

def main():
    listeGF(Path.home() / "Desktop", "1M")

def listeGF(p, k):
    if match := re.search(r"^(\d+)(K|M|G)$", k):
        size = int(match.group(1))
        if match.group(2) == "K": size *= 1024
        elif match.group(2) == "M": size *= 1048576
        elif match.group(2) == "G": size *= 1073741824
        for x in p.glob("**/*"):
            if x.stat().st_size >= size:
                print(x.name)
    else:
        raise SyntaxError("Improperly formatted size")
    
if __name__ == "__main__":
    main()