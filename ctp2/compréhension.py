#! /usr/bin/env python3

import random

def main():

    # matrix = [[(i * 2) + j for i in range(5)] for j in range(2)]
    # print(matrix)
    # print(transpose(matrix))

    L = list(range(10))
    random.shuffle(L)

    print(myqs(L))
    
def multiple(n):
    return [i for i in range(n) if not i % 5 or not i % 7]

def multiple_idx(l):
    return [elem for elem in l if elem % 5 == 0 or elem % 7 == 0]

def zipping(l, m):
    # this code does the same thing
    # l1 = []
    # for i in range(len(l)):
    #     l1.append((l[i], m[i]))
    # return l1
    return [(l[i], m[i]) for i in range(len(l))]

def transpose(m):
    return [[row[i] for row in m] for i in range(len(m[0]))]

def tens(n):
    return [[j * 10 + i for i in range(10)] for j in range(n + 1)]

def flatten(ll):
    return [elem for sub_list in ll for elem in sub_list]

def myqs(L):
    if len(L) <= 1: return L
    left = [elem for elem in L if elem < L[len(L)//2]]
    right = [elem for elem in L if elem > L[len(L)//2]]
    return myqs(left) + [L[len(L)//2]] + myqs(right)

if __name__ == "__main__":
    main()