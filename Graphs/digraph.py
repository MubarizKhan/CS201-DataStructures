class Digraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        self.g[node] = []

    def add_edge(self, src, dst):

        dic = self.g

        if src not in dic and dst not in dic:
            return False

        if dst in dic[src]:
            return 
        
        dic[src].append(dst)

    def __str__(self):
        return self.g



d = Digraph()
d.add_node("a")
d.add_node("b")
d.add_node("c")
d.add_node("d")
d.add_node("e")
d.add_node("f")
d.add_edge("a","b")
d.add_edge("a","c")
d.add_edge("b","d")
d.add_edge("c","e")
d.add_edge("c","f")


# print(d)
print(d.__str__())