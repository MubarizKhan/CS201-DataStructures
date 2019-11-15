class digraph():
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("node already exists")

        self.g[node] = []

    def add_edge(self, source, destination):
        
        if source not in self.g:
            raise ValueError("Source doesn't exist")

        if destination not in self.g:
            raise ValueError("Destination doesn't exist")

        nexts = self.g[source]
        if destination in nexts:
            return

        nexts.append(destination)

    
    def traversal(self, start):
        

        q = [start]
        visited = []

        while q:
            current = q.pop(0)

            if current in visited:
                continue

            print(current)

            visited.append(current)

            next_nodes = self.g[current]

            for n in next_nodes:
                q.append(n)

    
    def find_path(self, start, end, path = []):
        if start not in self.g:
            raise ValueError("Start doesn't exist in the graph")

        path.append(start)

        if start == end:
            return path

        for node in self.g[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)

                if new_path:
                    return new_path

        
        return None


d = digraph()
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
d.add_edge("b", "f")

print(d.find_path("a", "f"))


