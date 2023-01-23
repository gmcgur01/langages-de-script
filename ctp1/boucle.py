#! /usr/bin/env python3
import sys

def main():

    try:
        n = int(input())
    except ValueError:
        sys.exit("L'input n'est pas un numéro")

    print(sum(range(0, n + 1, 2)))

if __name__ == "__main__":
    main()