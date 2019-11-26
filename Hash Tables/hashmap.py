class hashmap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        return key % self.size

    def add(self, key, value):
        hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[hash] is None:
            self.map[hash] = [key_value]
            print("self.map was none before")
            return True

        else:
            for pair in self.map[hash]:
                if pair[0] == key:
                    pair[1] = value
                    print("Value updated")
                    return True
        
            self.map[hash].append(key_value)
            print("The new hash value is inserted")
            return True


    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for i in self.map[key_hash]:
                if i[0] == key:
                    return i[1]


        raise KeyError("This key value doesn't exist")


h = hashmap()
h.add(10, "hh")
h.add(20, "lOlo")
h.add(11, "Muaroz")
h.add(12,"saad")
h.get(10)