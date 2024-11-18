class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [' '] * size
    
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    
    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size
        
        for i in range(self.size):
            min_distance = float('inf')
            u = None
            for j in range(self.size):
                if not visited[j] and distances[j] < min_distance:
                    min_distance = distances[j]
                    u = j
                    
            if u is None:
                break
            visited[u] = True
            
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
        return distances

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
    print(f"Dijkstra's Algorithm starting from vertex {v}:\n")
    distances = g.dijkstra(v)
    for i, d in enumerate(distances):
        print(f"Shortest distance from D to {g.vertex_data[i]}: {d}")

if __name__ == "__main__":
    main()
