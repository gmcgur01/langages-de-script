#! /usr/bin/python3

def main():
    file = File()

    file.enque("1")
    file.enque("2")
    file.enque("3")
    file.enque("4")

    print(file)

    print(len(file))

    file = File(map(int, file))

    print(file)


class File:
    def __init__(self, values=[]):
        self.Tin = []
        self.Tout = list(values)

    def __len__(self):
        return len(self.Tin) + len(self.Tout)
    
    def __str__(self):
        return f"Pile: length = {len(self)} | {str(self.Tin[::-1] + self.Tout)}"

    def __iter__(self):
        self.ind = len(self)
        return self
    
    def __next__(self):
        if self.ind == 0:
            raise StopIteration
        self.ind -= 1
        if self.ind < len(self.Tin):
            return self.Tin[self.ind]
        else:
            return self.Tout[self.ind - len(self.Tin)]

    def enque(self, x):
        self.Tin.append(x)

    def deque(self):
        if len(self.Tout) != 0:
            return self.Tout.pop()
        elif len(self.Tin) != 0:
            for _ in range(len(self.Tin) - 1):
                self.Tout.append(self.Tin.pop())
            return self.Tin.pop()
        else:
            raise IndexError("Can't deque from an empty queue")

    

if __name__ == "__main__":
    main()