class digraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already exists")

        self.g[node] = []

    def add_edge(self, start, end):
        if start not in self.g:
            raise ValueError("Node doesn;t exist")

        if end not in self.g:
            raise ValueError("end doesnt't exist")

        nexts = self.g[start]
        if end in nexts:
            return
        print (start, "----", end)
        nexts.append(end)



    def traverse_graph(self, start):
        q = [start]
        visited = []

        while q:
            current = q.pop(0)

            if current in visited:
                continue

            print(current)
            visited.append(current)

            next_nodes = self.g[start]
            for i in next_nodes:
                q.append(i)


    def find_path(self, start, end, path = []):
        if start not in self.g:
            raise ValueError("node doesn't exist in find path")

        print(start, "--", end)
        path.append(start)
        if start == end:
            return path

        for node in self.g[start]:
            if node not in path:
                fp = self.find_path(node, end, path)
                if fp:
                    return path


        return None

    def find_all_paths(self, start, end, path = []):
        if start not in self.g:
            raise ValueError("node not in graoh")

        path.append(start)

        if start == end:
            return [path]

        all_paths = []

        for node in self.g[start]:
            if node not in path:
                all_new_paths = self.find_all_paths(node, end, path)
                for i in all_new_paths:
                    all_paths.append(i)


        return all_paths


    def find_shortest_path(self, start, end, path= []):
        if start not in self.g:
            raise ValueError("Starting nide does not exist")

        path.append(start)

        if start == end:
            return path

        shortest = None

        for node in self.g[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)
                if new_path:
                    print(shortest)
                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path


        return shortest

    


        

g = digraph()
l = ["a","b", "c", "d", "e", "f"]

for i in l:
    g.add_node(i)

edges = [("a", "b"), ("a", "c"), ("b", "c"), ("d", "a"), ("c", "d"), ("a", "d")]
for e in edges:
    g.add_edge(e[0], e[1])
# 
# g.traverse_graph("a")
# g.find_path("a", "d")
# print(g.find_all_paths("a", "d"))
print(g.find_shortest_path("a", "d"), ",")

