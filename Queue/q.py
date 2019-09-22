class queue:
    def __init__(self):
        self.size = 5
        self.q = list(range(self.size))
        self.i = 0
        self.o = 0
        self.is_empty = True
        self._is_full = False

    def _inc(self,val):
        if val + 1 == self.size:
            return 0
        else:
            return val + 1

    def enqueue(self, val):
        if self.is_full:
            raise IndexError("Queue is full")

        self.q[self.i] = val
        self.i = self._inc(self.i)

        if self.i == self.o:
            self._is_full = True
        
        self.is_empty = False

    def dequeue(self):
        if self.is_empty:
            raise Exception("FML")

        ret = self.q[self.o]
        self.o = self._inc(self.o)

        if self.i == self.o:
            self.is_empty = True
        
        self._is_full =False

        

