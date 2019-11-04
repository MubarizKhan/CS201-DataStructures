class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def get_str_hash(self, key):

        if type(key) == str:
            b = len(key) % self.size
            return b
        
        return

    def get_tuple_hash(self, key):

        if type(key) == tuple:
            b = len(key) % self.size
            return b

        return 

    def get_int_hash(self, key):

        if type(key) == int:
            return key % self.size
        
        return



    def _get_hash(self, key):
    
        if type(key) == int: 
            return self.get_int_hash(key)

        if type(key) == tuple:
            return self.get_tuple_hash(key)

        if type(key) == str:
            return self.get_str_hash(key)

        # self.get_int_hash(key)
        # self.get_tuple_hash(key)
        # self.get_str_hash(key)
        

    
    def __str__(self):
        ret = ""  
        for i, item in enumerate(self.map):
            if item is not None:
                ret += str(i) + ": " + str(item) + "\n"
        
        return ret


    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash]:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        raise KeyError(str(key) + " is not found!")

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True

        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        
            self.map[key_hash].append(key_value)
            return True


    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            raise KeyError(str(key))

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True


            

    


if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")


    h.add("sjds", "jiojceiosjs")
    h.add((1,2), "sjdsjsj")
    print(h)