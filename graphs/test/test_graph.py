import pytest
from graphs.graph import Graph
from graphs.graph_business_trip import business_trip

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
   

def test_business_trip():
    graph = Graph()
    vertex_a = graph.add_vertex('Metroville')
    vertex_b = graph.add_vertex('Pandora')
    vertex_c = graph.add_vertex('Naboo')
    vertex_d = graph.add_vertex('Arendelle')
    vertex_e = graph.add_vertex('New Monstropolis')
    vertex_f = graph.add_vertex('Narnia')

    graph.add_edge(vertex_a, vertex_b, 82)
    graph.add_edge(vertex_a, vertex_c, 26)
    graph.add_edge(vertex_a, vertex_d, 99)
    graph.add_edge(vertex_a, vertex_e, 105)
    graph.add_edge(vertex_a, vertex_f, 37)
    graph.add_edge(vertex_b, vertex_d, 150)
    graph.add_edge(vertex_d, vertex_e, 42)
    graph.add_edge(vertex_e, vertex_c, 73)
    graph.add_edge(vertex_c, vertex_f,250)

    actual = business_trip(graph, [vertex_a, vertex_b])
    expected = '$82'
    assert actual == expected

def test_business_trip_if_noedges():
    graph = Graph()
    vertex_a = graph.add_vertex('Metroville')
    vertex_b = graph.add_vertex('Pandora')
    vertex_c = graph.add_vertex('Naboo')
    vertex_d = graph.add_vertex('Arendelle')
    vertex_e = graph.add_vertex('New Monstropolis')
    vertex_f = graph.add_vertex('Narnia')

    graph.add_edge(vertex_a, vertex_b, 82)
    graph.add_edge(vertex_a, vertex_c, 26)
    graph.add_edge(vertex_a, vertex_d, 99)
    graph.add_edge(vertex_a, vertex_e, 105)
    graph.add_edge(vertex_a, vertex_f, 37)
    graph.add_edge(vertex_b, vertex_d, 150)
    graph.add_edge(vertex_d, vertex_e, 42)
    graph.add_edge(vertex_e, vertex_c, 73)
    graph.add_edge(vertex_c, vertex_f,250)

    actual = business_trip(graph, [vertex_f, vertex_d, vertex_c])
    expected = None
    assert actual == expected    


def test_depth_first():
    graph = Graph()

    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    vertex_e = graph.add_vertex('E')
    vertex_f = graph.add_vertex('F')
    vertex_g = graph.add_vertex('G')
    vertex_h = graph.add_vertex('H')

    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_d)
    graph.add_edge(vertex_b, vertex_d)
    graph.add_edge(vertex_b, vertex_c)
    graph.add_edge(vertex_c, vertex_g)
    graph.add_edge(vertex_d, vertex_e)
    graph.add_edge(vertex_d, vertex_f)
    graph.add_edge(vertex_d, vertex_h)
    graph.add_edge(vertex_h, vertex_f)

    actual = graph.depth_first(vertex_a)

    expected_output = "A, B, D, E, F, H, C, G"

    actual_output = ", ".join([node.value for node in actual])
    
    assert actual_output == expected_output

