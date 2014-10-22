import ast

class Meter:
    internal_id = 0
    HFID = 0
    LFID = 0
    monthly_energy_consumption = [0.0] #watt hours Wh
    unreported_high_frequency_consumption = 0.0
    unreported_low_frequency_consumption = 0.0
    neighbours = []
    def __init__(self, energy_usage, internal_id):
        self.energy_usage = energy_usage
        self.internal_id = internal_id
    def add_neighbour(other_meter):
        neighbour += other_meter


def parse_topology(topology):
    with open("topologies/" + str(topology) + ".txt", 'r') as file:
        string = file.read()
        delimiter = string.index("]") + 1
        nodes = ast.literal_eval(string[:delimiter])
        edges = ast.literal_eval(string[delimiter:])
        
        print "Nodes:\n" + str(nodes)
        print "Edges:\n" + str(edges)

def add_edge(meter_a, meter_b):
    


parse_topology("topologysmall")
            
    