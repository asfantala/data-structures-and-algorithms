# Challenge Find maximum value  
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(15).jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time Complexity: O(N), where N is number of nodes as every node of tree is traversed once by findMax()
- The space complexity of the findMax method in the Binary_tree class is O(h), where h is the height of the binary tree.## Solution
<!-- Show how to run your code, and examples of it in action -->
```

 def findMax(self, root):
        if root is None:
            return float('-inf')

        res = root.value
        lres = self.findMax(root.left)
        rres = self.findMax(root.right)
        if lres > res:
            res = lres
        if rres > res:
            res = rres
        return res
```