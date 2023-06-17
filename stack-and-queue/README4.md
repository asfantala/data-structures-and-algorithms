# Challenge validate brackets
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(13).jpg)

## Approach & Efficiency
- Big O 
The time complexity O(n): n is the length of the input string. This is because the function iterates through each character in the string exactly once.
The space complexity O(n):he space required by the stack is proportional to the number of opening brackets## Solution
<!-- Show how to run your code, and examples of it in action -->
```
def validate_brackets(string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[char] != stack.pop():
                return False

    return len(stack) == 0
```