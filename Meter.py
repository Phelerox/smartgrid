class Meter:
    internal_id = 0
    HFID = 0
    LFID = 0
    monthly_energy_consumption = [0.0] #watt hours Wh
    unreported_high_frequency_consumption = 0.0
    unreported_low_frequency_consumption = 0.0
    neighbours = []
    def __init__(self, internal_id, energy_usage):
        self.internal_id = internal_id
        self.energy_usage = energy_usage

    def add_neighbour(other_node):
        neighbours += other_node