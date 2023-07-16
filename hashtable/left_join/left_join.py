from hashtable import Hashtable
def left_join(synonyms:Hashtable, antonyms:Hashtable):
    """
    Given two hash maps, return a new data structure that holds the results of a LEFT JOIN operation.

    Args:
        synonyms: A hash map that has word strings as keys, and a synonym of the key as values.
        antonyms: A hash map that has word strings as keys, and antonyms of the key as values.

    Returns:
        The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
    """
    result = []
    synonyms_keys = synonyms.keys()
    for key in synonyms_keys:
        value = synonyms.get(key)
        if antonyms.has(key):
            result.append([key, value, antonyms.get(key)])
        else:
            result.append([key, value, None])
    return result
