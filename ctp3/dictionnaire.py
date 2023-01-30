#! /usr/bin/env python3

def main():
    print(list_to_dict(["a", "b", "c"]))
    print_dict(chars("aacababbcc"))
    d1 = {'r': 0.56, 't': 0.78, 'i': 0.23, 'u': 0.35}
    d2 = {'i': 5, 'v': 89, 'p': 65, 't': 21, 'b': 55}
    print(merge(d1, d2))
    print(inverse({"bananna": 1, "apple": 2, "grape": 3, "pineapple": 4}))

def list_to_dict(l):
    return {i:val for i, val in enumerate(l)}

# maybe not the best solution; inefficent
# def chars(w):
#     return {letter:w.count(letter) for letter in w}

def chars(w):
    ret = {}
    for letter in w:
        if letter not in ret.keys():
            ret[letter] = 1
        else:
            ret[letter] += 1
    return ret

def print_dict(d):
    for key in d.keys():
        print(key, d[key]) 

def merge(d1, d2):
    return {key:(d1[key], d2[key]) for key in d1.keys() if key in d2.keys()}

def inverse(d):
    for val in d.values():
        if list(d.values()).count(val) > 1:
            return {}
    return {d[key]:key for key in d.keys()}

if __name__ == "__main__":
    main()