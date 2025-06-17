class Solution:
    # graph 为图的邻接矩阵，start 为起始顶点
    def Prim(self, graph, start):
        size = len(graph)
        vis = set()
        dist = [float('inf') for _ in range(size)]
    
        ans = 0                             # 最小生成树的边权和
        dist[start] = 0                     # 初始化起始顶点到起始顶点的边权值为 0
    
        for i in range(1, size):            # 初始化起始顶点到其他顶点的边权值
            dist[i] = graph[start][i]
        vis.add(start)                      # 将 start 顶点标记为已访问
    
        for _ in range(size - 1):
            min_dis = float('inf')
            min_dis_pos = -1
            for i in range(size):
                if i not in vis and dist[i] < min_dis:
                    min_dis = dist[i]
                    min_dis_pos = i
            if min_dis_pos == -1:           # 没有顶点可以加入 MST，图 G 不连通
                return -1
            ans += min_dis                  # 将顶点加入 MST，并将边权值加入到答案中
            vis.add(min_dis_pos)
            for i in range(size):
                if i not in vis and dist[i] > graph[min_dis_pos][i]:
                    dist[i] = graph[min_dis_pos][i]
        return ans

points = [[0,0]]
graph = dict()
size = len(points)
for i in range(size):
    x1, y1 = points[i]
    for j in range(size):
        x2, y2 = points[j]
        dist = abs(x2 - x1) + abs(y2 - y1)
        if i not in graph:
            graph[i] = dict()
        if j not in graph:
            graph[j] = dict()
        graph[i][j] = dist
        graph[j][i] = dist
        

print(Solution().Prim(graph))