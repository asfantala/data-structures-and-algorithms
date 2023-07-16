import pytest
from graphs.graph import Graph

#Vertex can be successfully added to the graph
def test_add_vertex():      
    graph = Graph()
    expected = "A"
    actual = graph.add_vertex("A").value
    assert actual == expected

# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()
    node1 = graph.add_vertex("A")
    node2 = graph.add_vertex("B")
    graph.add_edge(node1, node2)
    expected = "B"
    actual = graph.adj_list[node1][0].vertex.value
    assert actual == expected

# A collection of all nodes can be properly retrieved from the graph
def test_get_vertices():
    graph = Graph()
    node1 = graph.add_vertex("A")
    node2 = graph.add_vertex("B")
    node3 = graph.add_vertex("C")
    expected = 3
    actual = len(graph.get_vertices())
    assert actual == expected

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors():
    graph = Graph()
    node1 = graph.add_vertex("A")
    node2 = graph.add_vertex("B")
    node3 = graph.add_vertex("C")
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    expected = ["B", "C"]
    actual = [edge.vertex.value for edge in graph.get_neighbors(node1)]
    assert actual == expected


# Neighbors are returned with the weight between nodes included

def test_get_neighbors_with_weight():
    graph = Graph()
    node1 = graph.add_vertex("A")
    node2 = graph.add_vertex("B")
    node3 = graph.add_vertex("C")
    graph.add_edge(node1, node2, 5)
    graph.add_edge(node1, node3, 10)
    expected = [(node2, 5), (node3, 10)]
    actual = [(edge.vertex, edge.weight) for edge in graph.get_neighbors(node1)]
    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_size():
    graph = Graph()
    node1 = graph.add_vertex("A")
    node2 = graph.add_vertex("B")
    node3 = graph.add_vertex("C")
    expected = 3
    actual = graph.size()
    assert actual == expected

# A graph with only one node and edge can be properly returned

def test_size_one_node():
    graph = Graph()
    node1 = graph.add_vertex("A")
    graph.add_edge(node1, node1)
    expected = 1
    actual = graph.size()
    assert actual == expected

    
def test_breadth_first():
    graph = Graph()

    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    vertex_e = graph.add_vertex('E')

    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_c)
    graph.add_edge(vertex_b, vertex_d)
    graph.add_edge(vertex_c, vertex_d)
    graph.add_edge(vertex_c, vertex_e)
    graph.add_edge(vertex_d, vertex_e)

    traversal_order = graph.breadth_first(vertex_a)
    expected_order = [vertex_a, vertex_b, vertex_c, vertex_d, vertex_e]
    assert traversal_order == expected_order
   

