#! /usr/bin/env python3

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 2, 3, 4, 4]
    print(same_elements(l1, l2))

    print(letters())

    print(to_list({"a", "c", "b", "f", "d", "e"}))

    print(even({1, 2, 3, 4, 5, 6, 7, "ajsdop"}))

    
def same_elements(l1, l2):
    return set(l1) == set(l2)

def letters():
    return {letter for letter in input().lower() if letter.isalpha()}

# def letters():
#     s = set()
    
#     for letter in input().lower():
#         if letter.isalpha():
#             s.add(letter)

#     return s

def to_list(s):
    return sorted(list(s))

def even(s):
    return {num for num in s if isinstance(num, int) and num % 2 == 0}

if __name__ == "__main__":
    main()