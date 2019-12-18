class tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(tree):
    def __init__(self, val, parent = None):
        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        if self.val["val"] > val["val"]:
            if self.left is None:
                new_node = BST(val,parent = self)
                print("Inserted at the left", new_node.val)
                self.left = new_node
            else:
                self.left.insert(val)

        else:
            if self.right is None:
                new_node = BST(val, parent= self)
                print("Inserted at the right", new_node.val)
                self.right = new_node

            else:
                self.right.insert(val)

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

        if self.parent.left == self:
            self.parent.left = node

        if self.parent.right == self:
            self.parent.right = node


    def replace_w_node(self, node):
        self.set_for_parent(node)
        node.parent = self.parent
        self.parent = None
        return node.find_root()
    # def dfs_appl


    def delete(self, val):
        if self.val == val:
            if self.parent is None and self.right is None and self.left is None:
                return None

            if self.left is None and self.right is None:
                self.set_for_parent(None)
                print(self.val)
                return self.find_root()

            if self.right is None:
                return self.replace_w_node(self.left)

            if self.left is None:
                return self.replace_w_node(self.right)

            successor = self.right.find_min()
            self.val = successor.val
            return self.right.delete(successor.val)

        else:
            if val[1] < self.val[1]:
                if self.left is not None:
                    return self.left.delete(val)
                else:
                    return self.find_root()

            else:
                if self.right is not None:
                    return self.right.delete(val)
                else:
                    return self.find_root()


    def dfs_apply(self, fn):
        fn(self)

        if self.left:
            self.left.dfs_apply(fn)

        if self.right:
            self.right.dfs_apply(fn)

    def bfs(self):
        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)
            print (current.val)

            if current.left:
                to_visit.append(current.left)

            if current.right:
                to_visit.append(current.right)


class performsum:
    def __init__(self):
        self.sum = 0

    def process(self, node):
        self.sum += node.val

    def get_sum(self):
        print(sum)
        return sum

    def reset_sum(self):
        self.sum = 0

d = {
    "name": "n",
    "val":1
}

d2 = {
    "name": "n2",
    "val":12
}

t = BST()
t.insert(d)
t.insert({4: "5"})
# t.insert(20)
# t.insert(7)

# t.delete(7)

# t.bfs()

p = performsum()
# p.reset_sum()
t.dfs_apply(p.process)
print(p.get_sum())