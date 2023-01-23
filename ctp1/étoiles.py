#! /usr/bin/env python3
import sys

def main():
    
    try:
        n = int(input())
    except ValueError:
        sys.exit("L'input donné n'est pas un numéro")

    for i in range(1, n + 1):
        print("*" * i)

if __name__ == "__main__":
    main()