class Solution:
    # 思路 1：动态规划 + 三维基本思路
    def twoDCostPackMethod1(self, weight: [int], volume: [int], value: [int], W: int, V: int):
        size = len(weight)
        dp = [[[0 for _ in range(V + 1)] for _ in range(W + 1)] for _ in range(size + 1)]
    
        # 枚举前 i 组物品
        for i in range(1, N + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举背包装载容量
                for v in range(V + 1):
                    # 第 i - 1 件物品装不下
                    if w < weight[i - 1] or v < volume[i - 1]:
                        # dp[i][w][v] 取「前 i - 1 件物品装入装载重量为 w、装载容量为 v 的背包中的最大价值」
                        dp[i][w][v] = dp[i - 1][w][v]
                    else:
                        # dp[i][w][v] 取所有 dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1] 中最大值
                        dp[i][w][v] = max(dp[i - 1][w][v], dp[i - 1][w - weight[i - 1]][v - volume[i - 1]] + value[i - 1])
                        
        return dp[size][W][V]
        
    # 思路 2：动态规划 + 滚动数组优化
    def twoDCostPackMethod2(self, weight: [int], volume: [int], value: [int], W: int, V: int):
        size = len(weight)
        dp = [[0 for _ in range(V + 1)] for _ in range(W + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, N + 1):
            # 逆序枚举背包装载重量
            for w in range(W, weight[i - 1] - 1, -1):
                # 逆序枚举背包装载容量
                for v in range(V, volume[i - 1] - 1, -1):
                    # dp[w][v] 取所有 dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1] 中最大值
                    dp[w][v] = max(dp[w][v], dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1])
                    
        return dp[W][V]