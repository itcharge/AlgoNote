class Solution:
    def bellmanFord(self, graph, source):
        size = len(graph)
        dist = dict()
        
        for vi in graph:
            dist[vi] = float('inf')
        
        dist[source] = 0
        
        for i in range(size - 1):
            for vi in graph:
                for vj in graph[vi]:
                    if dist[vj] > graph[vi][vj] + dist[vi]:
                        dist[vj] = graph[vi][vj] + dist[vi]
        
        for vi in graph:
            for vj in graph[vi]:
                if dist[vj] > dist[vi] + graph[vi][vj]:
                    return None
        
        return dist
                    
                    
graph = {
    'a': {'b': -1, 'c':  4},
    'b': {'c':  2, 'd':  3, 'e':  2},
    'c': {},
    'd': {'b':  3, 'c':  5},
    'e': {'d': -3}
}
dist = Solution().bellmanFord(graph, 'a')
print(dist)