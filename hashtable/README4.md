<!-- Description of the challenge -->
# Left Join  

## white board 
![](./left_join.jpg)


## Approach & Efficiency

- the time complexity of the function is O(n), and the space complexity is also O(n), where n is the number of key-value pairs in the synonyms dictionary.

## Solution : 
```
def left_join(synonyms, antonyms):

    result = []
    for key, value in synonyms.items():
        result.append([key, value])
        if key in antonyms:
            result[-1].append(antonyms[key])
        else:
            result[-1].append(None)
    return result
```