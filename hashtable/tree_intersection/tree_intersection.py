from hashtable import Hashtable


def tree_intersection(tree1, tree2):
    '''
   Finds the intersection between two binary tree

   Args : tree1 The first binary 
          tree2 The second binary tree

    returns:
        A set of the values that are in the intersection for the two binary trees 
'''

    intersection = set()
    hash_table = Hashtable()

    # Insert all the nodes of tree1 into the hash table
    for node in tree1:
        hash_table.set(node, None)

    # Iterate over all the nodes of tree2 and check if they are present in the hash table
    for node in tree2:
        if hash_table.has(node):
            intersection.add(node)

    return intersection