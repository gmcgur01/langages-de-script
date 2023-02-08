#! /usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <nomfiche>")

    try:
        with open(sys.argv[1]) as file:
            graphe = parse(file)
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(graphe)

def parse(file):

    file.readline()
    header = file.readline().strip()

    weighted = False
    directed = False

    if header == "":
        return {}
    else:
        components = header.split()

        if len(components) > 2:
            weighted = True

        if components[1] == "oriente":
            directed = True

    file.readline()
    nodes = file.readline().split()

    graphe = {node : {} for node in nodes}

    file.readline()

    

    return graphe

if __name__ == "__main__":
    main()