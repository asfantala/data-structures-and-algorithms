from graphs.graph import Graph

def business_trip(graph, array_of_cities):
    '''
    Function called business_trip
    Arguments: graph (Graph object), array of city names
    Return: the cost of the trip (if it's possible) or None (if not)
    '''
    cost = 0

    for i in range(len(array_of_cities) - 1):
        city1 = array_of_cities[i]
        city2 = array_of_cities[i + 1]

        neighbors = graph.get_neighbors(city1)
        found_direct_flight = False

        for neighbor in neighbors:
            if neighbor.vertex == city2:
                cost += neighbor.weight
                found_direct_flight = True
                break

        if not found_direct_flight:
            return None

    return f'${cost}'




if __name__ == '__main__':
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


    print(business_trip(graph, [vertex_a, vertex_b]))
    print(business_trip(graph, [vertex_d, vertex_e, vertex_c]))
    print(business_trip(graph, [vertex_a, vertex_e]))
    print(business_trip(graph, [vertex_f, vertex_d, vertex_c]))
    print(business_trip(graph, [vertex_e, vertex_c, vertex_f]))
   
    



