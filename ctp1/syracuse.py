#! /usr/bin/env python3

import sys

def main():
    
    try:
        num = int(input())
        if num <= 0:
            sys.exit("Il faut que l'input soit positif")
    except ValueError:
        sys.exit("Il faut que l'input soit un numéro positif")

    while num != 1:
        num = (3 * num + 1) if num % 2 else (num // 2)
        print(num)

if __name__ == "__main__":
    main()