#CS2516, Eamon Gaharan, 122382926
# Vertex, Edge and Graph classes from CS2516 - though parts have been edited :)
from random import randint


class Vertex:
    # class for vertex objects
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

    # lower than function
    def __lt__(self, other):
        return self._element < other._element


class Edge:
    # class for edge objects
    def __init__(self, v, w, element, weight):
        self._edgelabel = 0
        self._vertices = (v, w)
        self._element = element
        self._weight = weight

    def __str__(self):
        return f'Label: {str(self._edgelabel)} | Vertices: {str(self._vertices[0])}-{str(self._vertices[1])} | weight: {self._weight}'

    # lower than function
    def __lt__(self, other):
        return self._weight < other._weight

    # returns the vertices on the edge
    def vertices(self):
        return self._vertices

    # returns the opposite vertex from another on an edge
    def opposite(self, v):
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    # returns the element of an edge
    def element(self):
        return self._element

    def start(self):
        return self._vertices[0]

    def end(self):
        return self._vertices[1]

class Graph:
    def __init__(self):
        self._structure = dict()

    # string method
    def __str__(self):
        hstr = ('|V| = ' + str(self.num_vertices()) +
                '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self.vertices():
            vstr += str(v) + '-'
        estr = '\nEdges:\n '
        k = 0
        for e in self.edges():  # Use edges() method to directly access edges list
            e._edgelabel = k
            k += 1
            estr += str(e) + '\n '
        return hstr + vstr + estr

    # --------------------------------------------------#
    # ADT methods to query the graph

    # returns the amount of vertices in graph object
    def num_vertices(self):
        return len(self._structure)

    # returns the amount of edges
    def num_edges(self):
        num = 0
        for v in self._structure:
            num += len(self._structure[v])
        return num // 2

    # returns the vertices
    def vertices(self):
        return [key for key in self._structure]

    # returns the edges
    def edges(self):
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    # adds an edge to the graph

    def add_edge(self, edge):
        v, w = edge.vertices()
        if v not in self._structure:
            self._structure[v] = dict()
        if w not in self._structure:
            self._structure[w] = dict()
        self._structure[v][w] = edge
        self._structure[w][v] = edge

    # adds a vertex
    def add_vertex(self, element):
        v = Vertex(element)
        self._structure[v] = dict()
        return v


    def is_connected(self):
        def dfs(vertex, visited):
            visited.add(vertex)
            for neighbor in self._structure[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        start_vertex = next(iter(self.vertices()))
        dfs(start_vertex, visited)
        return len(visited) == self.num_vertices()


def graphgenerator(numofgraphs):
    # Generating a random graph
    graphs = []

    # v= no of vertices
    # e= no of edges
    # ratio between these 2 attributes = the density of the graph
    v = int(input("Enter a number of vertices for this graph: "))
    e = int(input(
        f"Enter a number of edges for this graph (max={v * (v - 1)//2} min={v-1}): "))
    if e > v * (v - 1) // 2 or e < v-1:
        raise ValueError(
            f"Input value {e} is bigger than {v * (v - 1)//2} or less than {v}")

    while numofgraphs:
        graph = Graph()
        vertices = []

        # making vertices
        for i in range(v):
            vertex = Vertex(i)
            vertices.append(vertex)

        # making edges
        for k in range(e):
            if len(vertices) < 2:
                break
            i = randint(0, len(vertices) - 2)
            j = randint(i + 1, len(vertices) - 1)
            vertex1 = vertices[i]
            vertex2 = vertices[j]
            #random weight between 1-20 assigned to each edge
            weight = randint(1, 20)
            #each edge initialized with a label 0, this will be assigned when printing the graph (because it wouldnt print them in order when i assigned them here)
            edge = Edge(vertex1, vertex2, 0, weight)
            graph.add_edge(edge)

        numofgraphs -= 1
        graphs.append(graph)
    return graphs


"""numofgraphs=int(input('enter number of graphs to generate:'))
graphs=graphgenerator(numofgraphs)

for graph in graphs:
    print(graph.is_connected())
    print(graph)
"""