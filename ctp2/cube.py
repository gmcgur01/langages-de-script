#! /usr/bin/env python3

def main():
    if no_cube(input("Donne-moi un mot: ")):
        print("Ce mot n'a pas un cube!")
    else:
        print("Ce mot a un cube!")

def prefixes(w, long_max):
    return [w[0:i] for i in range(1, long_max + 1)]

def cube_prefixes(w):
    my_prefixes = prefixes(w, len(w)//3)
    for prefix in my_prefixes:
        if prefix * 3 == w[:len(prefix) * 3]:
            return True
    return False

def no_cube(w):
    for i in range(len(w) - 2):
        if cube_prefixes(w[i:]): 
            return False
    return True

if __name__ == "__main__":
    main()