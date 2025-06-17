class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    

class Solution:
    def Kruskal(self, edges, size):
        union_find = UnionFind(size)
        
        edges.sort(key=lambda x: x[2])
        
        res, cnt = 0, 1
        for x, y, dist in edges:
            if union_find.is_connected(x, y):
                continue
            ans += dist
            cnt += 1
            union_find.union(x, y)
            if cnt == size - 1:
                return ans
        return ans
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        edges = []
        for i in range(size):
            xi, yi = points[i]
            for j in range(i + 1, size):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append([i, j, dist])
                
        ans = Solution().Kruskal(edges, size)
        return ans
            