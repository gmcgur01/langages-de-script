class Graph:
    def __init__(self):
        self._edges = dict()

    def __len__(self):
        return len(self._edges)

    def __iter__(self):
        return iter(self._edges)

    def __getitem__(self, node):
        return self._edges[node]

    def add_node(self, node):
        if node in self._edges:
            raise ValueError(f"Le sommet {node} existe déjà dans le graphe")
        else:
            self._edges[node] = [] 

    def add_edge(self, src, dst, weight=None):
        if src not in self._edges:
            self.add_node(src)
        if dst not in self._edges:
            self.add_node(dst)
        self._edges[src].append((dst, weight))

    def __str__(self):
        ret = ""
        for sommet in self:
            ret += f"{sommet} -> {self._edges[sommet]}\n"
        return ret[:-1]

    def bellman_ford(self, start):
        dist = {}
        pred = {}

        for sommet in self:
            dist[sommet] = float("inf")
            pred[sommet] = None

        dist[start] = 0

        for _ in range(0, len(self)):
            for sommet in self:
                for edge in self._edges[sommet]:
                    if dist[edge[0]] > dist[sommet] + edge[1]:
                        dist[edge[0]] = dist[sommet] + edge[1]
                        pred[edge[0]] = sommet
        return dist, pred

if __name__ == "__main__":
    g = Graph()

    g.add_edge("s", "a", 10)
    g.add_edge("s", "e", 8)
    g.add_edge("e", "d", 1)
    g.add_edge("d", "a", -4)
    g.add_edge("d", "c", -1)
    g.add_edge("c", "b", -2)
    g.add_edge("b", "a", 1)
    g.add_edge("a", "c", 2)

    print(g)
    print(g.bellman_ford("s"))
