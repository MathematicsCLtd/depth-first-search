# Depth-first search (DFS)

A common brute-force algorithm that works well for a small number of nodes. It begins at the graph root and then explores every node from the root down a single path. It then backtracks and begins exploring the paths not taken until it reaches the root again.

## Implementation

This algorithm takes in a graph represented as an adjacency list (a dictionary where the keys are nodes and the values are lists of their neighbors), a starting node, and an optional set of visited nodes. It returns a list of visited nodes in the order they were visited.

The algorithm works by first marking the starting node as visited and adding it to the result list. It then recursively visits all unvisited neighbors of the starting node by calling dfs on each of them and extending the result list with the visited nodes in the order they were visited.

The visited set is used to avoid revisiting nodes and getting stuck in cycles. It is initialized to an empty set if not provided as an argument.

## Testing
* The first test case checks a simple example with a directed acyclic graph where the DFS starts from node 1 and visits all nodes in the graph.
* The second test case checks a more complex example with an undirected graph where the DFS starts from node 'A' and visits all nodes in the graph.
* The third test case checks a graph with a cycle, where the DFS starts from node 'A' and visits all nodes in the graph, while avoiding cycles.

## Visualizations
Run locally to see the graphs used in the test cases.
1. Directed graph
![Image of Directed Acyclic Graph] (/img/direct_graph_output.PNG)
2.
3.

## Use Cases
* Finding connected components: DFS can be used to find all the connected components in an undirected graph. Each connected component is a group of nodes that are reachable from each other.
* Detecting cycles: DFS can be used to detect cycles in a graph. If a back edge is encountered during the traversal, it indicates the presence of a cycle in the graph.
* Topological sorting: DFS can be used to perform a topological sort of a directed acyclic graph (DAG). A topological sort is an ordering of the nodes in a DAG such that for every directed edge (u, v), node u comes before node v in the ordering.
* Pathfinding: DFS can be used to find a path between two nodes in a graph. If a path exists between the two nodes, DFS will find it.
* Finding strongly connected components: DFS can be used to find all the strongly connected components in a directed graph. A strongly connected component is a group of nodes that are reachable from each other by following directed edges.
* Solving puzzles: DFS can be used to solve puzzles that can be modeled as a graph. For example, DFS can be used to solve mazes, Sudoku puzzles, and crossword puzzles.
* Data processing: DFS can be used to traverse hierarchical data structures such as trees and XML documents. It is often used in compilers and interpreters to generate code or interpret programs.
* Web crawling: DFS can be used to crawl the web by following hyperlinks between web pages.
