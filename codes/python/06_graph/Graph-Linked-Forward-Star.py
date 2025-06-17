class EdgeNode:                                 # 边信息类
    def __init__(self, vj, val):
        self.vj = vj                            # 边的终点
        self.val = val                          # 边的权值
        self.next = None                        # 下一条边
        
class Graph:
    def __init__(self, ver_count, edge_count):
        self.ver_count = ver_count              # 顶点个数
        self.edge_count = edge_count            # 边个数
        self.head = [-1 for _ in range(ver_count)]  # 头节点数组
        self.edges = []                         # 边集数组
    
    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count
    
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for i in range(len(edges)):
            vi, vj, val = edges[i]
            self.add_edge(i, vi, vj, val)
            
    # 向图的边集数组中添加边：vi - vj，权值为 val
    def add_edge(self, index, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
            
        edge = EdgeNode(vj, val)                # 构造边节点
        edge.next = self.head[vi]               # 边节点的 next 指向原来首指针
        self.edges.append(edge)                 # 边集数组添加该边
        self.head[vi] = index                   # 首指针指向新加边所在边集数组的下标
    
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
            
        index = self.head[vi]                   # 得到顶点 vi 相连的第一条边在边集数组的下标
        while index != -1:                      # index == -1 时说明 vi 相连的边遍历完了
            if vj == self.edges[index].vj:      # 找到了 vi - vj 边
                return self.edges[index].val    # 返回 vi - vj 边的权值
            index = self.edges[index].next      # 取顶点 vi 相连的下一条边在边集数组的下标
        return None                             # 没有找到 vi - vj 边
    
    # 根据链式前向星打印图的边
    def printGraph(self):
        for vi in range(self.ver_count):        # 遍历顶点 vi
            index = self.head[vi]               # 得到顶点 vi 相连的第一条边在边集数组的下标
            while index != -1:                  # index == -1 时说明 vi 相连的边遍历完了
                print(str(vi) + ' - ' + str(self.edges[index].vj) + ' : ' + str(self.edges[index].val))
                index = self.edges[index].next  # 取顶点 vi 相连的下一条边在边集数组的下标
                

graph = Graph(7, 7)
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)    
print(graph.get_edge(4, 3))
print(graph.get_edge(4, 5))
graph.printGraph()