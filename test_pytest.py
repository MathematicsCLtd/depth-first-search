import algorithm    # The code to test

def test_dfs_directed():
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [],
        5: [6],
        6: []
    }
    assert algorithm.dfs(graph, 1) == [1, 2, 4, 5, 6, 3]

def test_dfs_undirected():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert algorithm.dfs(graph, 'A') == ['A', 'B', 'D', 'E', 'F', 'C']

def test_dfs_cycle():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['B'],
        'E': ['F'],
        'F': []
    }
    assert algorithm.dfs(graph, 'A') == ['A', 'B', 'D', 'E', 'F', 'C']
