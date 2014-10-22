import ast

import Meter, Concentrator

meters = {}
concentrator = Concentrator()

def parse_topology(topology):
    with open("topologies/" + str(topology) + ".txt", 'r') as file:
        string = file.read()
        delimiter = string.index("]") + 1
        nodes = ast.literal_eval(string[:delimiter])
        edges = ast.literal_eval(string[delimiter:])
        for node in nodes:
            if node.isdigit():
                id = int(node)
                meters.put(id, Meter(id, 0)
        for edge in edges:
            if edge[0] == "concentrator":
                a = concentrator
            elif edge[0].isdigit():
                a = meters.get(int(edge[0]))
            if edge[1] == "concentrator":
                b = concentrator
            elif edge[1].isdigit():
                meters.get(int(edge[1]))
            a.add_neighbour(b)
            b.add_neighbour(a)


parse_topology("topologysmall")