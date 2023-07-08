from hashtable import Hashtable

def left_join(synonyms, antonyms):

    """
    Given two hash maps, return a new data structure that holds the results of a LEFT JOIN operation.

    Args:
        synonyms: A hash map that has word strings as keys, and a synonym of the key as values.
        antonyms: A hash map that has word strings as keys, and antonyms of the key as values.

    Returns:
        The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
    """

    # TODO: Implement this function.

    result = []
    for key, value in synonyms.items():
        result.append([key, value])
        if key in antonyms:
            result[-1].append(antonyms[key])
        else:
            result[-1].append(None)
    return result