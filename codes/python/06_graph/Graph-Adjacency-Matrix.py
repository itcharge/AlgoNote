class Graph:                                    # 基本图类，采用邻接矩阵表示
    # 图的初始化操作，ver_count 为顶点个数
    def __init__(self, ver_count):
        self.ver_count = ver_count              # 顶点个数
        self.adj_matrix = [[None for _ in range(ver_count)] for _ in range(ver_count)]  # 邻接矩阵
    
    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count
    
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
    
    # 向图的邻接矩阵中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        
        self.adj_matrix[vi][vj] = val
    
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")

        return self.adj_matrix[vi][vj]
    
    # 根据邻接矩阵打印图的边
    def printGraph(self):
        for vi in range(self.ver_count):
            for vj in range(self.ver_count):
                val = self.get_edge(vi, vj)
                if val:
                    print(str(vi) + ' - ' + str(vj) + ' : ' + str(val))
    

graph = Graph(5)
edges = [[1, 2, 5],[2, 1, 5],[1, 3, 30],[3, 1, 30],[2, 3, 14],[3, 2, 14],[2, 4, 26], [4, 2, 26]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()