#! /usr/bin/env python3
import re

def main():
    filtre4("foo.txt")

def filtre1(fichenom):
    with open(fichenom) as file:
        for line in file:
            if match := re.match(r"\w{8,12}\b", line):
                print(line, end="")

def filtre2(fichenom):
    with open(fichenom) as file:
        for line in file:
            if match := re.search(r"\btoto\b", line):
                print(line, end="")

def filtre3(fichenom):
    with open(fichenom) as file:
        for line in file:
            if match := re.search(r"(\btoto\b.*){3,}", line):
                print(line, end="")

def filtre4(fichenom):
    with open(fichenom) as file:
        for line in file:
            if match := re.search(r"\b([a-z]+)\b.*\b\1\b.*\b\1\b", line):
                print(line, end="")


        # for line in file:
        #     freq = {}
        #     words = line.split()
        #     for word in words:
        #         if match := re.fullmatch(r"[a-z]+", word):
        #             if word in freq:
        #                 freq[word] += 1
        #                 if freq[word] >= 3:
        #                     print(line, end="")
        #                     break
        #             else:
        #                 freq[word] = 1


if __name__ == "__main__":
    main()