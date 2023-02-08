#! /usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 2:
        frequence(sys.argv[1])
    elif len(sys.argv) == 3:
        try:
            frequence(sys.argv[1], int(sys.argv[2]))
        except ValueError:
            sys.exit(f"Usage: {sys.argv[0]} <nomfiche> [n]")
    else:
        sys.exit(f"Usage: {sys.argv[0]} <nomfiche> [n]")
    

def frequence(nomfiche, n=0):

    freq = {}

    try:
        with open(nomfiche) as file:
            for line in file:
                words = line.strip().split(" ")
                for word in words:

                    # split each space-seperated words into words only 
                    # containing letters
                    words_to_add = [word.lower()]

                    index = 0

                    while index < len(words_to_add[-1]):
                        c = words_to_add[-1][index]
                        if not c.isalpha():
                            clean, rest = words_to_add[-1].split(c, 1)
                            words_to_add[-1] = clean
                            words_to_add.append(rest)
                            index = 0
                        else:
                            index += 1
                    
                    for word_to_add in words_to_add:
                        if word_to_add.isalpha() and len(word_to_add) > n:
                            if word_to_add in freq:
                                freq[word_to_add] += 1
                            else:
                                freq[word_to_add] = 1
    except FileNotFoundError:
        sys.exit(f"{nomfiche}: Unable to open file")

    size = len(freq)
    if size > 5:
        size = 5

    for _ in range(size):
        word = max(freq, key= lambda x: freq[x])
        print(word, freq[word])
        del freq[word]

if __name__ == "__main__":
    main()