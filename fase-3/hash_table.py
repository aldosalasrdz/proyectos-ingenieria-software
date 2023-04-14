class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, val):
        index = self.hash_function(key)
        slot = self.table[index]
        for i, (k, v) in enumerate(slot):
            if k == key:
                slot[i] = (key, v + val)
                return
        slot.append((key, val))

    def get(self, key):
        index = self.hash_function(key)
        slot = self.table[index]
        for k, v in slot:
            if k == key:
                return v
        return None

    def count_collisions(self):
        collisions = 0
        for slot in self.table:
            if len(slot) > 1:
                collisions += len(slot) - 1
        return collisions
