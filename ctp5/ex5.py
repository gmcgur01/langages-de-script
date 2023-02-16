#! /usr/bin/env python3

from pathlib import Path

def main():
    print(AncetreC(Path.cwd(), Path.home() / "Desktop"))

def AncetreC(p1, p2):
    if p1 in p2.parents:
        return p1
    for parent in p1.parents:
        if parent in p2.parents or parent == p2:
            return parent
    return None

if __name__ == "__main__":
    main()