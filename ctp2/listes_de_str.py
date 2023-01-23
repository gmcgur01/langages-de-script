#! /usr/bin/env python3

def main():
    # print(without_e(["eat", "sit", "rat"]))
    print(nstutter("eat sit sit sit rat"))

def without_e(l):
    return [word for word in l if "e" not in word]

def nstutter(string):
    words = string.split(" ")
    new_sentence = [word for i, word in enumerate(words) if word != words[i - 1]]
    return new_sentence

if __name__ == "__main__":
    main()