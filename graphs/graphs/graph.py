from collections import deque

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
    
    def breadth_first(self, start_node):
        '''
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection
        
        '''
        visited = set()
        traversal_order = []

        queue = deque()
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)

            neighbors = self.adj_list[current_node]
            for neighbor in neighbors:
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    queue.append(neighbor.vertex)

        return traversal_order

    # def breadth_first(self, node1):
    #     '''
    #     Arguments: node1
    #     Returns: A collection of nodes in the order they were visited.
    #     '''
    #     nodes = []
    #     breadth = Queue()
    #     visited = set()

    #     breadth.enqueue(node1)
    #     visited.add(node1)

    #     while not breadth.is_empty():
    #         front = breadth.dequeue()
    #         nodes.append(front)

    #         for edge in self.adj_list[front]:
    #             child = edge.vertex
    #             if child not in visited:
    #                 visited.add(child)
    #                 breadth.enqueue(child)

    #     return nodes







if __name__ ==  '__main__':
    
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('B', 'E')
        graph.add_edge('C', 'F')
        graph.add_edge('E', 'F')

        # Testing the breadth_first method
        traversal = graph.breadth_first('A')
        print(traversal)



   
    
    
    