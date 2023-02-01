#! /usr/bin/env python3
import random
import time

def main():
    # l = [random.randint(0, 5) for _ in range(10)]
    # table = init_table(10)
    # for elem in l:
    #     add_elt(elem, 10, table)
    # print(table)
    # suppr(1, 10, table)
    # print(table)

    hash_benchmark(100, 10000, 1000)

def init_table(n):
    return [None for _ in range(n)]

def add_elt(x,n,t):
    for i in range(n):
        if t[(x + i) % n] == None:
            t[(x + i) % n] = x
            return True
        if t[(x + i) % n] == x:
            return True
    return False

def suppr(x,n,t):
    for i in range(n):
        if t[(x + i) % n] == x:
            t[(x + i) % n] = None
            return True
        if t[(x + i) % n] == None:
            return False
    return False

def in_table(x,n,t):
    for i in range(n):
        if t[(x + i) % n] == None:
            return False
        if t[(x + i) % n] == x:
            return True
    return False

def test_hash(n,l):
    table = init_table(n)
    for elem in l:
        add_elt(elem, n, table)
    for elem in l:
        if not in_table(elem, n, table):
            return False
    return True

def test_set(l):
    s = {elem for elem in l}
    for elem in l:
        if not elem in l:
            return False
    return True

def hash_benchmark(k,m,n):
    l = [random.randint(0, m) for _ in range(k)]

    hash_start = time.time()
    assert(test_hash(n,l))
    hash_end = time.time()

    set_start = time.time()
    assert(test_set(l))
    set_end = time.time()

    print(f"test_hash: {hash_end - hash_start}")
    print(f"test_set: {set_end - set_start}")

main()