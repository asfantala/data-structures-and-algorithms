class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value
    
    
class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        '''
        add vertex
        Arguments: value
        Returns: The added vertex
        Add a vertex to the graph
    '''
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    
    def add_edge(self,node1, node2, weight=0):
        '''
        add edge
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def size(self):
        '''
        Arguments: none
        Returns the total number of vertices in the graph
        0 if there are none
        '''
        num_of_vertices = len(self.adj_list.keys())
        if num_of_vertices == 0 :
            return 0
        else:
            return num_of_vertices
    
    def get_vertices(self):
        '''
        Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no vertices
        '''
        vertices = self.adj_list.keys()
        if len(vertices) == 0:
            return []
        else:
            return vertices
    
    def get_neighbors(self, node):
        '''
        Arguments: vertex
        Returns a collection of edges connected to the given vertex
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
        '''
        return self.adj_list[node]
    
    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output    


if __name__ ==  '__main__':
    
        graph1 = Graph()

        a = graph1.add_vertex("A")
        b = graph1.add_vertex("B")
        c = graph1.add_vertex("C")
        d = graph1.add_vertex("D")

        graph1.add_edge(a,b)
        graph1.add_edge(a,c)
        graph1.add_edge(c,b)
        graph1.add_edge(d,b)
        graph1.add_edge(d,c)

        print(graph1)



   
    
    
    