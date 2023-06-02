#! /usr/bin/env python3

import json
import graph

def main():
    # dic = json.load(open("stops.json", "rb"))
    # for stop in dic.values():
    #     print(f"Stop name: {stop['stop_name']}")

    # print(Transport("stops.json", "timetable.json"))

    print(stop_to_id("Nation", "stops.json"))


class Transport(graph.Graph):
    def __init__(self, stops_fichenom, timetable_fichenom):
            super().__init__()
            stops = json.load(open(stops_fichenom, "rb"))
            for stop in stops:
                 self.add_node(stop)
            timetable = json.load(open(timetable_fichenom, "rb"))
            for key in timetable:
                 source, destination = key.split(", ")
                 self.add_edge(source, destination, timetable[key])

def stop_to_id(stop_name, stops_fichenom):
    stops = json.load(open(stops_fichenom, "rb"))

    ret = set()

    for id in stops:
        if stops[id]["stop_name"] != stop_name:
            continue
        if stops[id]["route"] == None:
            continue
        if not stops[id]["route"]["num"].isnumeric():
            continue
        if int(stops[id]["route"]["num"]) > 14:
            continue
        ret.add(id)

    return ret

def shortest_path(source, destination):
    source_ids = stop_to_id(source)
    destination_ids = stop_to_id(destination)

    ratp = Transport("stops.json", "timetable.json")

    for id in source_ids:
        dist, pred = ratp.bellman_ford(id)
        # TODO finish this shit



if __name__ == "__main__":
    main()