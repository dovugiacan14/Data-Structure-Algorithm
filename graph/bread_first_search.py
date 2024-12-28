from collections import deque, defaultdict 

class Graph:
    """
        V: number of nodes
        visit[]: mark visited nodes 
    """
    def __init__(self, V): 
        self.V   = V 
        self.adj = defaultdict(list)  # create DSLK in graph 

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def BFS(self, s): 
        result = []
        visited = [False] * self.V
        queue  = deque()

        # source peak s 
        visited[s] = True 
        queue.append(s)

        while queue: 
            s = queue.popleft()
            #print(s, end= " ")
            result.append(s)

            for n in self.adj[s]:
                if not visited[n]:
                    visited[n] = True 
                    queue.append(n)
        return result
            
        

if __name__ == "__main__":
    g = Graph(15)

    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1,4)
    g.addEdge(2,5)
    g.addEdge(2,6)
    g.addEdge(4,7)
    g.addEdge(4,8)
    g.addEdge(4,9)
    g.addEdge(6,10)
    g.addEdge(6,11)
    g.addEdge(7,11)
    g.addEdge(8,12)
    g.addEdge(8,13)
    g.addEdge(9,14)

    print("Following is Breadth First Traversal (starting from vertex 2):")
    r = g.BFS(1)
    for i in r:
        print(i, end="->")

    
