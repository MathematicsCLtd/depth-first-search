def dfs(graph, start, visited=None):
    """
    Perform Depth-First Search on a graph starting from a given node.

    :param graph: The graph to search represented as an adjacency list.
    :type graph: dict
    :param start: The node to start the search from.
    :type start: int or str
    :param visited: A set of visited nodes to avoid cycles. Defaults to an empty set.
    :type visited: set
    :return: A list of visited nodes in the order they were visited.
    :rtype: list
    """
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
