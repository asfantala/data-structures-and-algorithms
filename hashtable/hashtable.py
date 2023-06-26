class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """
        Arguments: key
        Returns: Value associated with that key in the table.
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def has(self, key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return True
        return False

    def keys(self):
        """
        Returns: Collection of keys

        """
        keys = []
        for bucket in self.table:
            for kvp in bucket:
                keys.append(kvp[0])
        return list(set(keys))

    def hash(self, key):
        """
        Arguments: key
        Returns: Index in the collection for that key
        """
        return self._hash(key)