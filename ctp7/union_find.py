#! /usr/bin/env python3

def main():
    uf = UnionFind()

    uf.add_node("a")
    uf.add_node("b")
    uf.add_node("c")

    print(uf.find(0))
    print(uf.find(1))
    print(uf.find(2))

    uf.union(0, 1)

    print(uf.find(0))
    print(uf.find(1))
    print(uf.find(2))


class UnionFind:
    def __init__(self):
       self.nodes = []
       self.parents = []

    def add_node(self, data):
        index = len(self.nodes)
        self.nodes.append(data) 
        self.parents.append(index)

    
    def find(self, index):
        if self.parents[index] != index:
            return self.find(self.parents[index])
        return index
    
    def union(self, x, y):
        self.parents[self.find(y)] = self.find(x)

if __name__ == "__main__":
    main()