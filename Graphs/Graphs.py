class digraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already exists")

        self.g[node] = []

    def add_edge(self, src, dest):
        if src not in self.g:
            raise ValueError("Source doesn't exist in the graph")

        if dest not in self.g:
            raise ValueError("Destination doesn't exist in the graph")

        if dest in self.g[src]:
            return

        self.g[src].append(dest)
    
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

            for n in next_nodes:
                q.append(n)

    def find_path(self, start, end, path = []):
        if start not in self.g:
            raise ValueError("Source node not in graph")

        print (start + "," + end)

        path.append(start)
        if start == end:
            return path
        
        for node in self.g[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
        
        return None

    def find_all_paths(self, start, end, path = []):

        

        if start not in self.g:
            raise ValueError("Starting node not in graph")

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


    def find_top_three(self, start, end, path = []):

        if start not in self.g:
            raise ValueError("Source node not in graph")

        path.append(start)
        
        
        high = []
        h = [None]
        sh = [None]
        th = [None]

        if start == end:
            high.append(path)

        for node in self.g[start]:

            if node not in path:

                    all_new_paths = self.find_top_three(node, end, path)
                    # if h is None or sh is None or th is None:
                    # if h is None:
                    #     if sh is None:
                    #         if th is None:
                    #             h = []
                    #             sh = []
                    #             th = []
                        

                        
                        
                    for i in all_new_paths:
                        
                        if h is None or sh is None or th is None or len(all_new_paths) is not None:
                            if len(all_new_paths) > len(h):
                                if len(all_new_paths) > len(sh):
                                    if len(all_new_paths) > len(th):
                                        th = sh
                                        sh = h
                                        h = all_new_paths
                                        high[0] = h

                            if len(all_new_paths) > len(sh):
                                if len(all_new_paths) > len(th):
                                    th = sh
                                    sh = all_new_paths
                                    high[1] = sh

                            if len(all_new_paths) > len(th):
                                th = all_new_paths
                                high[2] = th
        print (high)
        return high
                        

                # for i in all_new_paths:
                #     all_paths.append(i)
                #     for j in all_new_paths:

    def find_shortest_path(self,start, end, path = []):
        if start not in self.g:
            raise ValueError("diesnt exist")


        path.append(start)

        if start == end:
            return path

        shortest = None

        for node in self.g[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)

                if new_path:

                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path

        print (shortest)
        return shortest    










obj = digraph()
list = ['a', 'b', 'c','d','e','f']
for n in list:
    obj.add_node(n)

edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'd'),
    ('d', 'c'),
    ('d', 'e'),
    ('e', 'f'),
    ('f', 'c'),
    ('b', 'a'),
    ('b', 'f'),
    ('a', 'f'),
    ('f', 'c')


]

for n in edges:
    obj.add_edge(n[0], n[1])

obj.traverse_graph('b')
obj.find_path('b','d')

# print(obj.find_all_paths('b', 'f'))
# print(obj.find_shortest_path('b', 'f'))

print(obj.find_top_three('a','f'))





            