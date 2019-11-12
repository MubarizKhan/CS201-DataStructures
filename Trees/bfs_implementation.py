class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(node):
    def __init__(self, val,  parent = None):

        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        
        if val < self.val:
            if self.left is None:
                self.left = BST(val, self)
                print("Added")
            else:
                self.left.insert(val)


        else:
            if self.right is None:
                self.right = BST(val, self)
                print("Added to right")
            else:
                self.right.insert(val)



    def bfs(self):
        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            print(current.val)

            if current.left:
                to_visit.append(current.left)

            if current.right:
                to_visit.append(current.right)







bst = BST(20)
bst.insert(11)
bst.insert(22)
bst.insert(5)


bst.bfs()






    