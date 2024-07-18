#CS2516, Eamon Gaharan, 122382926
import heapq
from graphassignment import *
import time

class primHeap:
    def prim_heap(self, graph):
        mst = []
        pq = []  # Priority queue using heapq
        vertextoedge = {}
        visited = set()

        start_vertex = list(graph.vertices())[0]
        #print("start vertex:"+str(start_vertex))
        visited.add(start_vertex)
        self.edges_2_queue(pq, vertextoedge, graph, start_vertex)

        
        while pq:
            edge_weight, edge, vertex = heapq.heappop(pq)
            if vertex not in visited:
                visited.add(vertex)
                mst.append(edge)
                self.edges_2_queue(pq, vertextoedge, graph, vertex)

        return mst

    #adding edges to queue function
    def edges_2_queue(self, pq, vertextoedge, graph, vertex):
        for edge in graph.get_edges(vertex):
            adjvertex = edge.opposite(vertex)
            if adjvertex not in vertextoedge or edge._weight < vertextoedge[adjvertex][0]:
                heapq.heappush(pq, (edge._weight, edge, adjvertex))
                vertextoedge[adjvertex] = (edge._weight, edge, vertex)


class PrimUL:
    def prim_unsorted(self, graph):
        mst = []
        pq = []  # Priority queue as an unsortedlist
        vertextoedge = {}
        visited = set()

        start_vertex = list(graph.vertices())[0]
        #print("\nstart vertex:"+str(start_vertex))
        visited.add(start_vertex)
        self.edges_2_queue(pq, vertextoedge, graph, start_vertex)

        while pq:
            pq.sort()  # Sort the unsorted list, not needed for heap as its orders itself
            edge_weight, edge, vertex = pq.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                mst.append(edge)
                self.edges_2_queue(pq, vertextoedge, graph, vertex)

        return mst

    #adding edges to queue function
    def edges_2_queue(self, pq, vertextoedge, graph, vertex):
        for edge in graph.get_edges(vertex):
            adjvertex = edge.opposite(vertex)
            if adjvertex not in vertextoedge or edge._weight < vertextoedge[adjvertex][0]:
                pq.append((edge._weight, edge, adjvertex))
                vertextoedge[adjvertex] = (edge._weight, edge, vertex)


#testint the algorithms
if __name__ == "__main__":
    #the number of graphs being generated and tested
    h=graphgenerator(1)
    
    k=0
    htotaltime=0
    ultotaltime=0
    for i in h:
        g=i
        #printing each  graph if needed
        """print('\n\n\ngraph:'+ str(k))
        print(g)"""

        #calculating the time for heap implementation of each graph
        starttime1=time.time()
        primheap = primHeap()
        mst_heap = primheap.prim_heap(g)
        endtime1=time.time()

        #printing the min spanning tree for heap implementation of each graph
        """print("Prim's MST using heap based PQ:")
        for edge in mst_heap:
            print(edge)
        print(len(mst_heap))"""

        #calculating the time for UL implementation of each graph
        starttime2=time.time()
        primunsorted = PrimUL()
        mst_unsorted = primunsorted.prim_unsorted(g)
        endtime2=time.time()

        #printing the min spanning tree for Ul implementation of each graph
        """print("\nPrim's MST using unsorted list for PQ:")
        for edge in mst_unsorted:
            print(edge)
        print(len(mst_unsorted))"""

        k+=1

        #summing up the times and storing them
        heaptime=endtime1-starttime1
        ulisttime=endtime2-starttime2
        htotaltime+=heaptime
        ultotaltime+=ulisttime


    #getting avg by dividing the total times by the amount of runs
    heapavg=htotaltime/k
    ulistavg=ultotaltime/k


    print("\nAverage time for both implementations of prims algorithm on the given graphs:")
    print("Heap implementation time average: "+str(heapavg))
    print("Unsorted list implementation avg: "+str(ulistavg))
    

    #heapavg returns a shorter time than ulistavg the bigger the graph
    #however the opposite is true the smaller the graph 