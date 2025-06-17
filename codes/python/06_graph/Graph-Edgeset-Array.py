class EdgeNode:                                 # 边信息类
    def __init__(self, vi, vj, val):
        self.vi = vi                            # 边的起点
        self.vj = vj                            # 边的终点
        self.val = val                          # 边的权值
        
class Graph:                                    # 基本图类，采用边集数组表示
    def __init__(self):
        self.edges = []                         # 边数组
        
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
            
    # 向图的边数组中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        edge = EdgeNode(vi, vj, val)            # 创建边节点
        self.edges.append(edge)                 # 将边节点添加到边数组中
        
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        for edge in self.edges:
            if vi == edge.vi and vj == edge.vj:
                val = edge.val
                return val
        return None
    
    # 根据边数组打印图
    def printGraph(self):
        for edge in self.edges:
            print(str(edge.vi) + ' - ' + str(edge.vj) + ' : ' + str(edge.val))
            
graph = Graph()
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()