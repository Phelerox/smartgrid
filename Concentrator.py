class Concentrator:
    associated_substation = 0
    neighbours = []

    def __init__(self):
        pass

    def add_neighbour(self, other_node):
        self.neighbours.append(other_node)