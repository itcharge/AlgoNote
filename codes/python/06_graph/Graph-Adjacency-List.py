class EdgeNode:                                 # 边信息类
    def __init__(self, vj, val):
        self.vj = vj                            # 边的终点
        self.val = val                          # 边的权值
        self.next = None                        # 下一条边

class VertexNode:                               # 顶点信息类
    def __init__(self, vi):
        self.vi = vi                            # 边的起点
        self.head = None                        # 下一个邻接点
        
class Graph:
    def __init__(self, ver_count):
        self.ver_count = ver_count
        self.vertices = []
        for vi in range(ver_count):
            vertex = VertexNode(vi)
            self.vertices.append(vertex)
    
    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count
    
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
    
    # 向图的邻接表中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
            
        vertex = self.vertices[vi]
        edge = EdgeNode(vj, val)
        edge.next = vertex.head
        vertex.head = edge

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        
        vertex = self.vertices[vi]
        cur_edge = vertex.head
        while cur_edge:
            if cur_edge.vj == vj:
                return cur_edge.val
            cur_edge = cur_edge.next
        return None
        
    # 根据邻接表打印图的边
    def printGraph(self):
        for vertex in self.vertices:
            cur_edge = vertex.head
            while cur_edge:
                print(str(vertex.vi) + ' - ' + str(cur_edge.vj) + ' : ' + str(cur_edge.val))
                cur_edge = cur_edge.next
                
graph = Graph(7)
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()