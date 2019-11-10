class treenode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class tree:
    def __init__(self):
        self.root = None
    

    def insert(self, val, node):
        if self.root is None:
            self.root = treenode(val)
            return self

        if node is None:
            node = treenode(val)
            return node

        if val < node.val:
            node.left = self.insert(val, node.left)
            return node

        if val > node.val:
            node.right = self.insert(val, node.right)
            return node
        
        


    def dfs_inorder(self,node):
        #node = self.root
        
        if node is None:
            return

        if node.left != None:
            self.dfs_inorder(node.left)

        print (node.val)

        if node.right != None:
            self.dfs_inorder(node.right)


t = tree()
ls = [10,4,6,12,2,14]
for i in ls:
    t.insert(i, t.root)

t.dfs_inorder(t.root)
