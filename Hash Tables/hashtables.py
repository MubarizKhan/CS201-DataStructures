class hashmap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def get_hash(self, key):
        return key % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True

        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    print("Updating")
                    pair[1] = value
                    return True
        
            self.map[key_hash].append(key_value)
            return True

    def __str__(self):
        ret = ""
        for i, item in enumerate(self.map):
            if item is not None:
                ret += str(i) + ": " + str(item) + "\n"
        return ret

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        else:
            raise KeyError("cant find key !")


h = hashmap()

h.add(11, "")
h.add(41, "www")
h.add(32, "df")
h.add (2, "dfcmskd")
# h.add(1, "")

print(h)