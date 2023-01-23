#! /usr/bin/env python3

def main():
    s = "Hello, World!"
    for c in s:
        if c.lower() in "aeiouy":
            print(c, end="")
    print("")

if __name__ == "__main__":
    main()