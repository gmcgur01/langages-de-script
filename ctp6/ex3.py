#! /usr/bin/env python3
import re
from pathlib import Path

def main():
    popular_name(Path.cwd() / "prenoms.txt", 5)

def parse_line(line):
    if match := re.match(r"(\d+),(\d+),(\d+),(.+)", line):
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)), match.group(4))

def parse_file(path):

    ret = {}

    with open(path) as file:
        for line in file:
            parsed_line = parse_line(line)
            if parsed_line != None:
                key = (parsed_line[3], parsed_line[0])
                if key not in ret or parsed_line[1] > ret[key]:
                    ret[key] = parsed_line[1]
            # else:
                # print(line, end="")

    return ret

def name_frequency(d):

    ret = {}
    for key in d:
        if key[0] in ret:
            ret[key[0]] += d[key]
        else:
            ret[key[0]] = d[key]
    return ret


def popular_name(fname, n):

    d = name_frequency(parse_file(fname))

    l = sorted(d.keys(), key=lambda x: d[x], reverse=True)[:n]

    for name in l:
        print(name, d[name])

if __name__ == "__main__":
    main()