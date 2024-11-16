class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [' '] * size
    
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    
    def print_graph(self):
        print('Adjasency Matrix')
        for i in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', i))
        print('\nVertex Data: ')
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data}")

def main():
    n=int(input())
    g = Graph(n)
    for i in range(n):
        vertex = input()
        g.add_vertex_data(i, vertex)
    
    m=int(input())
    for j in range(m):
        
