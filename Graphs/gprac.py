class digraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already in graph")

        self.g[node] = []

    def add_edge(self, src, dest):
        if src not in self.g or dest not in self.g:
            raise ValueError(">")

        if dest in self.g[src]:
            return
        
        self.g[src].append(dest)
        print ("EDGE ADDED")


    def traverse(self, start):
        if start not in self.g:
            raise ValueError("Start not in graph")

        q = [start]
        visited = []

        while q:
            current = q.pop(0)
            if current in visited:
                continue

            print (current)

            visited.append(current)

            for i in self.g[current]:
                q.append(i)


g = digraph()
nodes = ['a','b','c','d','e','f']
for i in nodes:
    g.add_node(i)


edges = [
    ('a', 'c'),
    ('a', 'd'),
    ('d', 'c'),

    ('c', 'f'),
    ('f', 'b'),

    ('b', 'e'),
    ('e', 'a'),

]

for i in edges:
    g.add_edge(i[0], i[1])

g.traverse('a')


