class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(treenode):
    def __init__(self, val, parent = None):
        super().__init__(val)
        self.parent = parent

    def insertion(self, val):
        if val < self.val:
            if self.left is None:
                new_node = BST(val, parent = self)
                self.left = new_node


            else:
                self.left.insertion(val)

        else:
            if self.right is None:
                new_node = BST(val, parent = self)
                self.right = new_node
            
            else:
                self.right.insertion(val)
                print("insert at right")

    def find_root(self):
        temp = self
        while temp.parent is not None:
            temp = temp.parent

        return temp

    def find_min(self):
        min_node = self
        if self.left is not None:
            min_node = find_min(self.left)

        return min_node

    def set_for_parent(self, node):
        if self.parent is None:
            return 
        if self.parent.right == self:
            self.parent.right = node

        if self.parent.left == self:
            self.parent.left = node
    
    def replace_with_node(self, node):
        self.set_for_parent(node)
        node.parent = self.parent
        self.parent = None
        return node.find_root()

    
    def delete(self, val):
        if self.parent is None and self.left is None and self.right is None and self.val == val:
            print("SR IS NONE")
            return None

        if self.val == val:
            if self.right is None and self.left is None:
                print("deleting leaf")
                self.set_for_parent(None)
                self.find_root()

        if self.right is None:
            print("SR IS NONE")
            return self.replace_with_node(self.left)

        if self.left is None:
            print("SL IS NONE")
            return self.replace_with_node(self.right)


        successor = self.right.find_min()
        self.val = successor.val
        
        print("deleting successor ")
        return self.right.delete(successor.val)

        if val < self.val:
            print("SR IS not NONE")
            if self.left is not None:
                return self.left.delete(val)
            else:
                return self.find_root()

        else:
            
            if self.right is not None:
                return self.right.delete(val)
            else:
                return self.find_root()

bst = BST(40)
lst = [11,12,45,55,66,5, 9]
for i in lst:
    bst.insertion(i)

bst.delete(66)
bst.delete(11)

    # def is_binary(self,root):
    #     def is_bst(self,min,max):
    #         if self.val <min:
    #             return False
    #         if self.val > max:
    #             return False

    #         left_is = True
    #         right_is = True

    #         if self.left:
    #             left_is = self.is_bst(treenode,min, max)

    #         if self.right:
    #             right_is = self.is_bst(treenode, max, min)

    #         return left_is and right_is
            
    #         if root is None:
    #             print("is bst")
    #             return True

    #         return is_bst(root, float('-inf'), float('inf'))





# b = treenode(40)
# b.left = treenode(10)
# b.right = treenode(1)

# print(b.is_binary(b))