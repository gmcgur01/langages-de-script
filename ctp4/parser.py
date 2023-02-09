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

    header = next_line(file)

    weighted = False
    directed = False

    if header == "":
        return {}
    else:
        components = header.split()

        comp_len = len(components)

        if comp_len < 2 or comp_len > 3:
            raise SyntaxError("Improperly formatted header")
        
        if comp_len == 3:
            weighted = True

        if components[1] != "oriente" and components[1] != "non-oriente":
            raise SyntaxError("Improperly formatted header")

        if components[1] == "oriente":
            directed = True

    if next_line(file).strip() != "Sommets:":
        raise SyntaxError("Sommets keyword not found")

    nodes = next_line(file).split()

    graphe = {node : set() for node in nodes}

    if next_line(file).strip() != "Transitions:":
        raise SyntaxError("Transitions keyword not found")

    while True:
        curr_edge = next_line(file).strip()
        if curr_edge == "":
            break
        parse_edge(curr_edge, graphe, weighted, directed)

    return graphe

def next_line(file):
    line = file.readline()
    while line != "" and line[0] == "%":
        line = file.readline()
    return line

def parse_edge(curr_edge, graphe, weighted, directed):
    if directed and not weighted:

        components = curr_edge.split()
        if len(components) != 3 or components[1] != "-->":
            raise SyntaxError("Improperly formatted edge")
        if components[0] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        if components[2] not in graphe:
            raise SyntaxError(f"{components[2]}: No such node exits")
        graphe[components[0]].add(components[2])

    if directed and weighted:

        components = curr_edge.split()
        if len(components) != 5 or components[1] != "--" or components[3] != "-->":
            raise SyntaxError("Improperly formatted edge")
        if components[0] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        if components[4] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        try:
            weight = float(components[2])
        except ValueError:
            raise SyntaxError(f"{components[2]}: Invalid edge weight")
        graphe[components[0]].add((components[4], weight))
        
    if not directed and not weighted:

        components = curr_edge.split()
        if len(components) != 3 or components[1] != "--":
            raise SyntaxError("Improperly formatted edge")
        if components[0] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        if components[2] not in graphe:
            raise SyntaxError(f"{components[2]}: No such node exits")
        graphe[components[0]].add(components[2])
        graphe[components[2]].add(components[0])

    if not directed and weighted:

        components = curr_edge.split()
        if len(components) != 5 or components[1] != "--" or components[3] != "--":
            raise SyntaxError("Improperly formatted edge")
        if components[0] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        if components[4] not in graphe:
            raise SyntaxError(f"{components[0]}: No such node exits")
        try:
            weight = float(components[2])
        except ValueError:
            raise SyntaxError(f"{components[2]}: Invalid edge weight")
        graphe[components[0]].add((components[4], weight))
        graphe[components[4]].add((components[0], weight))

if __name__ == "__main__":
    main()