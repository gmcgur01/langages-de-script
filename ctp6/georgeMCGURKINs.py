#! /usr/bin/env python3

import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <fichenom>")
    
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                if line.startswith("bip"):
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: impossible d'ouvrir le ficher")

if __name__ == "__main__":
    main()