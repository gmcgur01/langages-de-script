#! /usr/bin/env python3

import sys

def main():
    
    try:
        num = int(input())
    except ValueError:
        sys.exit("L'input n'est pas un numéro")
        
    if num > 0:
        print("positif")
    elif num < 0:
        print("negatif")
    else:
        print("zero")

if __name__ == "__main__":
    main()