#! /usr/bin/env python3

import random

def main():

    heap = Heap([random.randint(0,10000) for _ in range(100)])

    sorted_list = []

    while not heap.is_empty():
        sorted_list.append(heap.pop())

    print(sorted_list)

class Heap:

    def __init__(self, vals=[]):

        if vals == []:
            self.data = [None]
            self.size = 0
        else:
            self.data = [None] + vals
            self.size = len(vals)
            for i in reversed(range(1, self.size//2)):
                self.heapify(i)

    def __str__(self):
        return str(self.data[1:])

    def is_empty(self):
        return self.size == 0

    def top(self):
        if self.is_empty():
            raise IndexError("No top element in an empty heap")
        return self.data[1]
    
    def push(self, x):
        self.size += 1
        self.data.append(x)

        index = self.size
        while index != 1:
            if self.data[index] < self.data[index//2]:
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp
                index = index//2
            else:
                break

    def pop(self):

        temp = self.data[self.size]
        self.data[self.size] = self.data[1]
        self.data[1] = temp
        
        ret = self.data.pop()
        self.size -= 1

        self.heapify(1)

        return ret
    
    def heapify(self, index):

        while index < self.size//2:
            if self.data[index * 2] <= self.data[(index * 2) + 1]:
                new_index = index * 2
            else:
                new_index = (index * 2) + 1

            if self.data[new_index] < self.data[index]: 
                temp = self.data[new_index]
                self.data[new_index] = self.data[index]
                self.data[index] = temp
                index = new_index
            else:
                break

if __name__ == "__main__":
    main()