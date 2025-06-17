class Solution:
    def dfs_recursive(self, graph, u, visited):
        print(u)                        # 访问节点
        visited.add(u)                  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited:        # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursive(graph, v, visited)

    def dfs_stack(self, graph, u):
        print(u)                        # 访问节点 u
        visited, stack = set(), []      # 使用 visited 标记访问过的节点, 使用栈 stack 存放临时节点
        
        stack.append([u, 0])            # 将起始节点 u 以及节点 u 的下一个邻接节点下标放入栈中，下一次将遍历 graph[u][0]
        visited.add(u)                  # 将起始节点 u 标记为已访问
        
    
        while stack:
            u, i = stack.pop()          # 取出节点 u，以及节点 u 下一个将要访问的邻接节点下标 i
            
            if i < len(graph[u]):
                v = graph[u][i]         # 取出邻接节点 v
                stack.append([u, i + 1])# 将节点 u 以及节点 u 的下一个邻接节点下标 i + 1 放入栈中，下一次将遍历 graph[u][i + 1]
                if v not in visited:    # 节点 v 未访问过
                    print(v)            # 访问节点 v
                    stack.append([v, 0])# 将节点 v 以及节点 v 的下一个邻接节点下标 0 放入栈中，下一次将遍历 graph[v][0]
                    visited.add(v)      # 将节点 v 标记为已访问
        

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于递归实现的深度优先搜索
visited = set()
Solution().dfs_recursive(graph, "A", visited)


# 基于堆栈实现的深度优先搜索
Solution().dfs_stack(graph, "A")