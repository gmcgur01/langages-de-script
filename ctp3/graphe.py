#! /usr/bin/env python3

time = 0
Pre = {}
Post = {}
Marquage = {}

def main():
    graphe = Graphe(["x1", "x2", "x3", "x4"], [("x1", "x2"), ("x1", "x3"), ("x2", "x4"), ("x4", "x4"), ("x3", "x4"), ("x3", "x1")])
    PrintG(graphe)
    DFS(graphe)
    print(Pre)
    print(Post)

def Graphe(S, L):
    res = {}
    for sommet in S:
        res[sommet] = {arc[1] for arc in L if arc[0] == sommet}

    return res       

def PrintG(D):
    for sommet in D.keys():
        print (f"Sommet: {sommet} - Arcs: ", end="")
        for arc in D[sommet]:
            print(arc, end=" ")
        print("")

def DFS(G):
    global time, Marquage

    time = 1
    for u in G.keys():
        Marquage[u] = False
    for u in G.keys():
        if Marquage[u] == False:
            explorer(G, u)

def explorer(G, u):
    global time, Marquage, Pre, Post
    
    Marquage[u] = True
    Pre[u] = time
    time += 1
    for v in G[u]:
        if Marquage[v] == False:
            explorer(G, v)
    Post[u] = time
    time += 1

main()