class WeightedDiGraph: 
    def __init__(self): 
        self.g = {} 
        
    def add_node(self, node): 
        if node in self.g: 
            raise ValueError("Node already in graph")
            
        self.g[node] = [] 

    def add_edge(self, src, dest, weight1,weight2): 
        if src not in self.g: 
            raise ValueError("Source node not in graph")
        if dest not in self.g: 
            raise ValueError("Destination node not in graph")
            
        nexts = self.g[src]
        if dest in nexts: 
            return 
        
        nexts.append((dest, weight1,weight2))
        



g = WeightedDiGraph()

nodes = ["isb","pwr","lhe","khi","gjr","fsb","mtn","skr","hbd","bnu","qta","mnw"]

for node in nodes:
    g.add_node(node)
    
edges = [
        ("isb","pwr",140,180),
        ("pwr","gjr",360,390),
        ("gjr","lhe",130,96),
        ("gjr","fsb",200,147),
        ("lhe","mtn",260,345),
        ("fsb","mtn",200,240),
        ("mtn","skr",400,440),
        ("skr","hbd",290,330),
        ("hbd","khi",160,162),
        ("pwr","bnu",240,198),
        ("bnu","qta",660,683),
        ("qta","skr",320,390),
        ("pwr","mnw",290,240),
        ("mnw","mtn",320,299),
        ("isb","gjr",230,220),
        ("isb","lhe",260,375),
]

for edge in edges:
    g.add_edge(edge[0],edge[1],edge[2],edge[3])




import pprint
pprint.pprint(g.g)



def find_shortest_dijkstra(self, src, dest): 
    
    to_visit = list(self.g.keys())
  
    inf = float('inf')
    dists = { node: inf for node in to_visit }
    dists[src] = 0 
  
    
    best_paths = {} 
    best_paths[(src, src)] = [src]
    

    while to_visit:
        
        current = min(to_visit,key = lambda node : dists[node])
       
        
        if dists[current] == inf:
            break
            
        nexts = self.g[current]
        unvisited = []
        for n in nexts:
            if n[0] in to_visit:
                unvisited.append(n)
                
        for n in unvisited:
            node = n[0]
            time  = n[1]
            dist = n[2]
                        
            old_time  = dists[node]
            new_time = dists[current] + time 
            #print(new_time)
            
            if new_time < old_time :
                dists[node] = new_time
                
                path_to_current = best_paths[(src, current)][:]   # need a copy 
                best_paths[(src, node)] = path_to_current
                best_paths[(src, node)].append(node)
          
        to_visit.remove(current)
        
    path = best_paths[(src,dest)]
    distance = 0

    for i in range(0,len(path)):
        src = path[i]
        dst = path[i+1]
        
        for j in  self.g[src]:
            if dst == j[0]:
                #print(j)
                value = j[2]
                distance += value
                
        if i+1 == len(path)-1 :
            break
        
   
    #      PATHS  , TIME   , DISTANCE
    return (path,dists[dest],distance)
    

    
WeightedDiGraph.find_shortest_dijkstra = find_shortest_dijkstra



print(find_shortest_dijkstra(g,"isb","khi"))
