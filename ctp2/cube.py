#! /usr/bin/env python3

def main():
    print(prefixes("hello world", 7))

def prefixes(w, long_max):
    return [w[0:i] for i in range(1, long_max + 1)]


if __name__ == "__main__":
    main()