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
        if val < self.val:
            if self.left is None:
                new_node = BST(val, parent= self)
                self.left = new_node

            else:
                self.left.insert(val)

        else:
            if self.right is None:
                new_node = BST(val, parent= self)
                self.right = new_node

            else:
                self.right.insert(val)

    def find_root(self):
        if self.parent is None:
            return None

        temp = self.parent
        while temp.parent is not None:
            temp = temp.parent

        return temp

    def set_for_node(self, node):
        if self.parent is None:
            return 

        if self.parent.left == self:
            self.parent.left = node

        if self.parent.right == self:
            self.parent.right = node

    def replace_with_node(self, node):
        self.set_for_node(node)
        node.parent = self.parent
        self.parent = None
        node.find_root()

    def find_min(self):
        min_node = self
        if self.left:
            min_node = self.find_min(self.left)

        return min_node


    def delete(self, val):
        if self.left is None and self.right is None and self.parent is None and self.val == val:
            return None

        if self.val == val:
            if self.left is None and self.right is None:
                print ("///")
                self.set_for_node(None)
                return self.find_root()

            if self.left is None:
                print ("///")
                self.set_for_node(self.right)

            if self.right is None:
                print ("///")
                self.set_for_node(self.left)


            successor = self.right.find_min()
            self.val = successor.val

            return self.right.delete(successor.val)


        if self.val < val:
            if self.left:
                print ("///")
                self.left.delete(val)
            else:
                return self.find_root()

        else:
            if self.right:
                self.right.delete(val)
            else:
                return self.find_root()

bst = BST(40)
l = [55, 11, 22, 65,2,77]
for i in l:
    bst.insert(i)

bst.delete(11)
bst.delete(65)


