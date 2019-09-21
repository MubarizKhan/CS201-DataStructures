class Queue:
    def __init__(self):
        self.size = 5
        self.i = 0
        self.o = 0
        self.is_empty = True
        self.is_full = False

        self.q = list(range(self.size))

    def _inc(self, val):
        if val + 1 == self.size:
            return 0
        else:
            return val + 1

    def enqueue(self, val):
        if self.is_full:
            raise IndexError("List is full!")

        self.q[self.i] = val
        self.i = self._inc(self.i)

        if self.i == self.o:
            self.is_full = True

        self.is_empty = False

    def dequeue(self):
        if self.is_empty:
            raise IndexError("List is empty!")

        ret = self.q[self.o]
        self.o = self._inc(self.o)

        if self.o == self.i:
            self.is_empty = True
        
        self.is_full = False


    def __str__(self):
        return str(self.q) + ", in: " +  str(self.i) + "out: " + str(self.o)

        
q = Queue()
q.enqueue(1)
q.enqueue(3)
q.dequeue()

print (q)