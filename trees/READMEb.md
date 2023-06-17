# Challenge Breadth first  
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(17).jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
 - breadth_first function is O(n), where n is the number of nodes in the binary tree.
 -  dequeuing time to O(1) 
 -  The space complexity of the breadth_first function is O(w), where w is the maximum width of the binary tree
## Solution
<!-- Show how to run your code, and examples of it in action -->

```
def breadth_first(self):
        result = []
        if self.root is None:
            return result

        queue = []  # Initialize a list-based queue
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
    


```