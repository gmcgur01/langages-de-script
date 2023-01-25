#! /usr/bin/env python3

def main():
    print(is_balanced(input("Donne-moi un mot: ")))

def is_balanced(s):
    pile = []
    for lettre in s:
        if lettre in "({[":
            pile.append(lettre)
        elif lettre in ")}]":
            if not len(pile): return False
            if lettre == ")" and pile[-1] != "(": return False
            if lettre == "]" and pile[-1] != "[": return False
            if lettre == "}" and pile[-1] != "{": return False
            pile.pop()
    return len(pile) == 0


if __name__ == "__main__":
    main()