class VertexNode:                               # 顶点信息类
    def __init__(self, vi):
        self.vi = vi                            # 顶点
        self.adj_edges = dict()                 # 顶点的邻接边
        
class Graph:
    def __init__(self):
        self.vertices = dict()                   # 顶点
    
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
    
    # 向图中添加节点
    def add_vertex(self, vi):
        vertex = VertexNode(vi)
        self.vertices[vi] = vertex
    
    # 向图的邻接表中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):        
        if vi not in self.vertices:
            self.add_vertex(vi)
        if vj not in self.vertices:
            self.add_vertex(vj)
        
        self.vertices[vi].adj_edges[vj] = val
        
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if vi in self.vertices and vj in self.vertices[vi].adj_edges:
            return self.vertices[vi].adj_edges[vj]
        return None
    
    # 根据邻接表打印图的边
    def printGraph(self):
        for vi in self.vertices:
            for vj in self.vertices[vi].adj_edges:
                print(str(vi) + ' - ' + str(vj) + ' : ' + str(self.vertices[vi].adj_edges[vj]))


graph = Graph()
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()