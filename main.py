import ast

from Meter import *
from Concentrator import *

meters = {}
concentrator = Concentrator()

def parse_topology(topology):
    with open("topologies/" + str(topology) + ".txt", 'r') as file:
        string = file.read()
        delimiter = string.index("]") + 1
        nodes = ast.literal_eval(string[:delimiter])
        edges = ast.literal_eval(string[delimiter:])

        for node in nodes:
            if isinstance(node, int):
                id = int(node)
                meters.update({id:Meter(id, 0)})

        for edge in edges:
            if edge[0] == "concentrator":
                a = concentrator
            elif isinstance(edge[0], int):
                a = meters.get(int(edge[0]))
            if edge[1] == "concentrator":
                b = concentrator
            elif isinstance(edge[1], int):
                b = meters.get(int(edge[1]))

            a.add_neighbour(b)
            b.add_neighbour(a)


parse_topology("topologysmall")