#! /usr/bin/env python3

import time

def main():
    s = "Speedy Gonzales" * 10000
    o = "ee"

    start = time.time()
    count(s,o)
    end = time.time()
    print("My implementation: ", end - start)

    start = time.time()
    s.count(o)
    end = time.time()
    print("Their implementation: ", end - start)

def count_blanks(s):
    return s.count(" ")

def is_palindrome(s):
    return s == s[::-1]

def count(s, o):
    i = 0
    end = len(s)
    width = len(o)
    ret = 0

    while i + width <= end:
        if s[i: i + width] == o:
            ret += 1
            i += width
        else:
            i += 1
    return ret

if __name__ == "__main__":
    main()