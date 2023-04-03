#! /usr/bin/python3 

def main():
    print("hello world")
    mystack = Stack()
    print(mystack)
    mystack.push("Hello")
    mystack.push("world!")
    print(mystack)
    print(mystack.head())
    mystack.pop()
    print(mystack)
    print(mystack.is_empty())
    mystack.pop()
    print(mystack)
    print(mystack.is_empty())

class Stack:

    def __init__(self):
        self.data = []
        self.size = 0

    def __str__(self):
        return str(self.data)
    
    def push(self, x):
        self.size += 1
        self.data.append(x)

    def pop(self):
        if self.size == 0:
            raise IndexError("Can't pop from an empty stack")
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        return self.size == 0
    
    def head(self):
        if self.size == 0:
            raise IndexError("No head :(")
        return self.data[self.size - 1]
    
if __name__ == "__main__":
    main()