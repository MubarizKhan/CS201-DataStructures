class DiGraph:
    def __init__(self):
        self.g = {}

    def add_node(self,node):
        self.g[node] = []

    def add_edge(self, src, dst):
        dic = self.g
        if src not in dic and dst not in g:
            return False
        if dst in self.g[src]:
            return
        dic[src].append(dst)

    def __str__(self):
        return self.g


d = DiGraph()
d.add_node("212")
d.add_node("24")
d.add_node("43253")
d.add_node("4523")
d.add_node("423")
d.add_node("561")
d.add_edge("212","24")
d.add_edge("43253","4523")
d.add_edge("423","561")
# d.add_edge("c","e")
# d.add_edge("c","f")


print(d.__str__())

class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(treenode):
    def __init__(self, val, parent = None):
        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        if self.val > val:
            if self.left is None:
                new_node = BST(val, parent = self)
                print("SL IS NONE")
                self.left = new_node

            else:
                self.left.insert(val)

        else:
            if self.right is None:
                new_node = BST(val, parent = self)
                self.right = new_node
            else:
                self.right.insert(val)


    def dfs_apply(self, fn):
        fn(self)

        if self.left:
            self.left.dfs_apply(fn)

        if self.right:
            self.right.dfs_apply(fn)





    def get_height(self):

        # p = performsum()

        height = 1
        lf = 0
        rf = 0

        if self.left is None and self.right is None:
            return height

        if self.left:
            # lf = self.left.dfs_apply(p.process)
            lf += 1
            self.left.get_height()

        if self.right:
                # rf += 1
            # rf =  self.right.dfs_apply(p.process)
            rf += 1
            self.right.get_height()

        if self.left and self.right is None:
            hx = max(lf, rf)
            print(hx, "<-")
            return hx + 1

    def sum(self):
        # sum = 0
        print(self.val)
        

        if self.left:
            # sum = 0 
            sum 
            self.left.sum()

        if self.right:
            self.right.sum()

        if self.left is None and self.right is None:
            return sum




b = BST(78)
b.insert(11)
b.insert(123)
b.insert(73)
b.insert(89)

b.get_height()
b.sum()

