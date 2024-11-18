class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [' '] * size
    
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    
    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        
        for i in range(self.size - 1):
            for j in range(self.size):
                for k in range(self.size):
                    if self.adj_matrix[j][k] != 0:
                        if distances[j] + self. adj_matrix[j][k] < distances[k]:
                            distances[k] = ditances[j] + self.adj_matrix[j][k]
                            predecessors[k] = j
                            print(f"Relaxing edge {self.vertex_data[j]}->{self.vertex_data[k]}, Updated distance to {self.vertex_data[k]} : {distances[k]}")
        
        for j in range(self.size):
            for k in range(self.size):
                if (self.adj_matrix[j][k] != 0):
                    if distances[j] + self.adj_matrix[j][k] < distances[k]:
                        return (True, None, None)
        
        return (False, distances, distances)
    
    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        curr = self.vertex_data.index(end_vertex)
        while curr is not None:
            path.insert(0, self.vertex_data[curr])
            curr = predecessors[curr]
            if curr == self.vertex_data.index(start_index):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)
        
def main():
    n=int(input())
    g = Graph(n)
    for i in range(n):
        vertex = input()
        g.add_vertex_data(i, vertex)
    
    m=int(input())
    for j in range(m):
        edgefrom = int(input())
        edgeto = int(input())
        weight = int(input())
        g.add_edge(edgefrom, edgeto, weight)
     
    v=input()
    print(f"Belmann-ford Algorithm starting from vertex {v}:\n")
    negative_cycle, distances, predecessors = g.bellman_ford(v)
    if not negative_cycle:
        for i,d in enumerate(distances):
            if d != float('inf'):
                path = g.get_path(predecessors, v, g.vertex_data[i])
                print(f"{path}, Distance: {d}")
            else:
                print(f"No path from {v} to {g.vertex_data[i]}, Distance: Infinity")

if __name__ == "__main__":
    main()
