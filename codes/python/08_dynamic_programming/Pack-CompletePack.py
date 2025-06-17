class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def completePackMethod1(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(w // weight[i - 1] + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
        
        return dp[size][W]
    
    # 思路 2：动态规划 + 状态转移方程优化
    def completePackMethod2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                else:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                    dp[i][w] = max(dp[i - 1][w], dp[i][w - weight[i - 1]] + value[i - 1])
                    
        return dp[size][W]
    
    # 思路 3：动态规划 + 滚动数组优化
    def completePackMethod3(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                
        return dp[W]