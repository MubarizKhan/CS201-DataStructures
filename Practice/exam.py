class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class bst(treenode):
    def __init__(self, val, parent = None):
        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                new_node = bst(val, parent = self)
                print("inserted at righ")
                self.left = new_node

            else:
                self.left.insert(val)

        else:
            if self.right is None:
                new_node = bst(val, parent = self)
                print("inserted at righ")
                self.right = new_node
            else:
                self.right.insert(val)

    def min_max(self):
        minn = self.val
        maxx = self.val

        if self.left.val < minn:
            minn = self.left.val
            print(minn)

        if self.right.val > maxx:  
            maxx = self.right.val
            print(maxx)

        if self.left:
            self.left.min_max()

        if self.right:
            self.right.min_max()

        




t = bst(40)
l = [1,33,66,54,2, 63]

for i in l:
    t.insert(i)

t.min_max()



