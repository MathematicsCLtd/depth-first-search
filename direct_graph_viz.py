import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5],
    4: [],
    5: [6],
    6: []
}

# Create a NetworkX graph object
G = nx.DiGraph(graph)

# Define the node colors
node_colors = ['#F4D03F' if n == 1 else '#F5B7B1' if n in [4, 6] else '#D7BDE2' if n == 5 else '#AED6F1' for n in G.nodes()]

# Define the node labels
node_labels = {n: str(n) for n in G.nodes()}

# Define the edge labels
edge_labels = {(u, v): str(v) for u, v in G.edges()}

# Define the positions of the nodes using a spring layout
pos = nx.spring_layout(G)

# Draw the graph
nx.draw_networkx(G, pos, node_color=node_colors, with_labels=False)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=16)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, label_pos=0.25, rotate=False)

# Set the plot title
plt.title('Test Case 1')

# Show the plot
plt.show()
