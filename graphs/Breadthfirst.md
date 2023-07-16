# Challenge Graph 

### Whiteboard Process
![whiteboard](/breadthfirst.jpg)

### Approach & Efficiency
- The time complexity of the breadth-first search algorithm in the worst case is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph
- The space complexity of the algorithm in the worst case is O(V), where V is the number of vertices (nodes) in the graph.


### Solution

```
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

```
