#! /usr/bin/env python3

def main():
    test()

def test():
    L=[1,2,3,4]
    L1=L
    L2=L[:]
    L1[1]=18
    L2[1]=20
    print(L)
    print(L1)
    print(L2)

if __name__ == "__main__":
    main()