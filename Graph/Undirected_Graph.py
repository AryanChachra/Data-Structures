class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertex_data = ['']*size
        
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    
    def print_graph(self):
        print('Adjacency Matrix')
        for i in self.adj_matrix:
            print(' '.join(map(str, i)))
        print('Vertex data')
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data} ")

def main():
    n=int(input())
    g = Graph(n)
    for i in range(n):
        vertex = input()
        g.add_vertex_data(i,vertex)
    
    l=int(input())
    for j in range(l):
        edgefrom = int(input())
        edgeto = int(input())
        g.add_edge(edgeto, edgefrom)
    
    g.print_graph()

if __name__ == "__main__":
    main()
