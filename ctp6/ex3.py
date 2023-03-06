#! /usr/bin/env python3
import re

def main():
    with open("prenoms.txt") as file:
        for line in file:
            print(parse_line(line))

def parse_line(line):
    if match := re.match(r"(\d+),(\d+),(\d+),(\w+)", line):
        return (match.group(1), match.group(2), match.group(3), match.group(4))

if __name__ == "__main__":
    main()