import sys
from matplotlib import pyplot as plt

import networkx as nx

# sys.argv[1]: input file to use

def main():
    G = nx.Graph()

    # Load file and get data
    for line in open(sys.argv[1]):
        node, connections = line.split(':')
        for connection in connections.split():
            G.add_edge(node, connection)

    # Plot nodes
    nx.draw(G, with_labels=True)
    plt.show()

    # It is assumed that the minimum cut is for 
    # three edges and that there are only two components
    G.remove_edges_from(nx.minimum_edge_cut(G))
    first_component, second_component = nx.connected_components(G)

    return len(first_component) * len(second_component)

if __name__ == "__main__":
    print(main())