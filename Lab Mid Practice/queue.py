class queue:
    def __init__(self):
        self.size = 5
        self.q = list(range(self.size))
        self.out = 0
        self.i = 0
        self.is_empty = True
        self.is_full = False

    def inc(self, idx):
        if idx + 1 == self.size:
            return 0
        else:
            return idx + 1

    def enqueue(self, val):
        if self.is_full:
            raise Exception("List is full")

        self.q[self.i] = val
        self.i = self.inc(self.i)

        if self.i == self.out:
            self.is_full = True
        
        self.is_empty = False

    
    def dequeue(self):
        if self.is_empty:
            raise Exception("Is empty already")

        val = self.q[self.out]
        self.out = self.inc(self.out)

        if self.i == self.out:
            self.is_empty = True

        self.is_full = False

    def __str__(self):
        return str(self.q) + ", in: " + str(self.i) + ", out: " + str(self.out)


q = queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)

q.dequeue()
q.dequeue()
q.dequeue()


print(q)



