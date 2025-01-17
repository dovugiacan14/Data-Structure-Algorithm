from bread_first_search import Graph 

# 1. Find number of interconnected components in a graph
def find_connected_components(graph, n):
    visited = [False] * n
    components = 0
    for i in range(n):
        if not visited[i]:
            components += 1
            visited[i] = True
            r = graph.BFS(i)
            for j in r:
                visited[j] = True
    return components

if __name__ == "__main__":
    g = Graph(16)

    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(7, 9)
    g.addEdge(8, 10)
    g.addEdge(7, 8)
    g.addEdge(11, 12)
    g.addEdge(11, 13)
    g.addEdge(12, 14)
    g.addEdge(14, 15)
    g.addEdge(16, 16)

    print("Number of connected components: ", find_connected_components(g, 16))

