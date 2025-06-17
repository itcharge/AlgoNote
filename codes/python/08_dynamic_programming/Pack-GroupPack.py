class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def groupPackMethod1(self, group_count: [int], weight: [[int]], value: [[int]], W: int):
        size = len(group_count)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 组物品能取个数
                dp[i][w] = dp[i - 1][w]
                for k in range(group_count[i - 1]):
                    if w >= weight[i - 1][k]:
                        # dp[i][w] 取所有 dp[i - 1][w - weight[i - 1][k]] + value[i - 1][k] 中最大值
                        dp[i][w] = max(dp[i][w], dp[i - 1][w - weight[i - 1][k]] + value[i - 1][k])
                    
        return dp[size][W]
    
    # 思路 2：动态规划 + 滚动数组优化
    def groupPackMethod2(self, group_count: [int], weight: [[int]], value: [[int]], W: int):
        size = len(group_count)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量
            for w in range(W, -1, -1):
                # 枚举第 i - 1 组物品能取个数
                for k in range(group_count[i - 1]):
                    if w >= weight[i - 1][k]:
                        # dp[w] 取所有 dp[w - weight[i - 1][k]] + value[i - 1][k] 中最大值
                        dp[w] = max(dp[w], dp[w - weight[i - 1][k]] + value[i - 1][k])
                        
        return dp[W]
                
            