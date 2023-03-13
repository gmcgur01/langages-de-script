#! /usr/bin/env python3

import re
import ex3

def main():
    # print(proportion(ex3.name_frequency(ex3.parse_file("prenoms.txt"))))
    # print(proportion_of_population())
    most_popular_for_each_letter()

def count(d):
    count = 0
    m = ends_with_at_least_four_consecutive_consonants()
    for nom in d.keys():
        if m.search(nom.lower()) != None:
            count += 1
    return count

def proportion(d):
    count = 0
    m = compound_word()
    for nom in d.keys():
        if m.fullmatch(nom.lower()):
            count += 1
    return count / len(d.keys())

def proportion_of_population():
    d = ex3.parse_file("prenoms.txt")

    count = 0
    total = 0

    m = compound_word()

    for item in d.items():
        if item[0][1] >= 1905 and item[0][1] <= 2015:
            total += item[1]
            if m.fullmatch(item[0][0].lower()):
                count += item[1]

    return count / total

def is_square():
    return re.compile(r"^(\w+)\1$")

def contains_square_of_length_four():
    return re.compile(r"(\w{2,})\1")

def five_of_the_same_letter():
    return re.compile(r"(.).*\1.*\1.*\1.*\1")

def contains_at_least_four_consecutive_vowels():
    return re.compile(r"[aeiouy]{4,}")

def contains_at_least_four_consecutive_consonants():
    return re.compile(r"[^aeiouy'-]{4,}")

def ends_with_at_least_four_consecutive_consonants():
    return re.compile(r"[^aeiouy'-]{4}$")

def compound_word():
    return re.compile(r".+(?: |-).+")

def most_popular_for_each_letter():
    d = ex3.name_frequency(ex3.parse_file("prenoms.txt"))
    l = sorted(d.keys(), key=lambda x: d[x], reverse=True)

    for i in range(26):
        j = 0
        while(re.match(chr(97 + i), l[j].lower()) == None):
            j += 1
        print (chr(97 + i), ":", l[j])

if __name__ == "__main__":
    main()