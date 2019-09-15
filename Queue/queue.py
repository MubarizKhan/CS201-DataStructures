class Queue:
    def __init__(self):
        self.size = 5
        self.queue = list(range(self.size))
        self.i = 0
        self.o = 0

        self.is_empty = True
        self.is_full = False

    def _inc(self, val):
        if val + 1 == self.size:
            return 0
        else:
            return val + 1



    def enqueue(self, val):
        if self.is_full:
            raise IndexError("The Queue is full!")

        self.queue[self.i] = val
        self.i = self._inc(self.i)

        if self.i == self.o:
            self.is_full = True
        
        self.is_empty = False


    def dequeue(self):
        if self.is_empty:
            raise IndexError("Queue is empty!")

        ret = self.queue[self.o]
        self.o = self._inc(self.o)

        if self.i == self.o:
            self.is_empty = True

        self.is_full = False

    
    def __str__(self):
        return str(self.queue) + "In: " + str(self.i) + "Out: " + str(self.o)


Q = Queue()
Q.enqueue(1)
Q.enqueue(1)
Q.enqueue(1)
Q.enqueue(1)
Q.enqueue(1)

print(Q)

Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()


print(Q)
      




