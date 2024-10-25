class Graph:
    #adjacency list
    def __init__(self):
        self.graph={}
        self.directed = False

    def addVertex(self,vertex):
        #if vertex is not already present, initialise it with no edge
        if vertex not in self.graph:
            self.graph[vertex] = []
    def addEdge(self, src , dest):
        #add source and destination vertex to graph
        self.addVertex(src)
        self.addVertex(dest)

        #add the destination vertex to lost with edge of source
        self.graph[src].append(dest)
    #undirected
        if not self.directed:
            self.graph[dest].append(src)
    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")
    
    def bfs(self, startVertex):
        queue = [startVertex]
        is_visited = [startVertex]
        n=self.graph[startVertex]
        while queue:
            currentVertex = queue.pop()
            print(currentVertex , end = " ")

            for neighbour in self.graph[currentVertex]:
                if neighbour not in is_visited:
                    queue.append(neighbour)
                    is_visited.append(neighbour)

    def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end= " ")
            visited.append(vertex)
            for v in self.graph[vertex]:
                self.dfs(v,visited)

G=Graph()
G.addEdge("a","b")
G.addEdge("b","d")
G.addEdge("a","c")
G.addEdge("a","d")
G.addEdge("e","d")
G.addEdge("f","c")
G.addEdge("e","f")
G.displayGraph()
#G.bfs("a")
G.dfs("d",[])
