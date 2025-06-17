import collections

class Solution:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingDFS(self, graph: dict):
        visited = set()                     # 记录当前顶点是否被访问过
        onStack = set()                     # 记录同一次深搜时，当前顶点是否被访问过
        order = []                          # 用于存储拓扑序列
        hasCycle = False                    # 用于判断是否存在环
        
        def dfs(u):
            nonlocal hasCycle
            if u in onStack:                # 同一次深度优先搜索时，当前顶点被访问过，说明存在环
                hasCycle = True
            if u in visited or hasCycle:    # 当前节点被访问或者有环时直接返回
                return
            
            visited.add(u)                  # 标记节点被访问
            onStack.add(u)                  # 标记本次深搜时，当前顶点被访问
    
            for v in graph[u]:              # 遍历顶点 u 的邻接顶点 v
                dfs(v)                      # 递归访问节点 v
                    
            order.append(u)                 # 后序遍历顺序访问节点 u
            onStack.remove(u)               # 取消本次深搜时的 顶点访问标记
        
        for u in graph:
            if u not in visited:
                dfs(u)                      # 递归遍历未访问节点 u
        
        if hasCycle:                        # 判断是否存在环
            return []                       # 存在环，无法构成拓扑序列
        order.reverse()                     # 将后序遍历转为拓扑排序顺序
        return order                        # 返回拓扑序列
    
    def findOrder(self, n: int, edges):
        # 构建图
        graph = dict()
        for i in range(n):
            graph[i] = []
        for v, u in edges:
            graph[u].append(v)
        
        return self.topologicalSortingDFS(graph)
    
print(Solution().findOrder(2, [[1,0]]))
print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(1, []))