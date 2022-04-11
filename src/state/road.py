class Road:
    # Node pozisyonlari
    NODES = []

    # Hangi node hangisine bagli
    # EDGES = []

    # Nodelarin tanjantlari (gerek olmayabilir)
    
    EDGE_LENGTHS = []
    EDGE_SPEED_LIMITS = []

    def get_data(self, data):
        nodes = data[0]
        edges = data[1]
        tangests = data[2]


class Node:
    connected_nodes = []
    start_tangent = None
    end_tangent = None
