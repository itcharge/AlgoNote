class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def multiplePackMethod1(self, weight: [int], value: [int], count: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(min(count[i - 1], w // weight[i - 1]) + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
                    
        return dp[size][W]
    
    # 思路 2：动态规划 + 滚动数组优化
    def multiplePackMethod2(self, weight: [int], value: [int], count: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(min(count[i - 1], w // weight[i - 1]) + 1):
                    # dp[w] 取所有 dp[w - k * weight[i - 1]] + k * value[i - 1] 中最大值
                    dp[w] = max(dp[w], dp[w - k * weight[i - 1]] + k * value[i - 1])
                
        return dp[W]
    
    # 思路 3：动态规划 + 二进制优化
    def multiplePackMethod3(self, weight: [int], value: [int], count: [int], W: int):
        weight_new, value_new = [], []
        
        # 二进制优化
        for i in range(len(weight)):
            cnt = count[i]
            k = 1
            while k <= cnt:
                cnt -= k
                weight_new.append(weight[i] * k)
                value_new.append(value[i] * k)
                k *= 2
            if cnt > 0:
                weight_new.append(weight[i] * cnt)
                value_new.append(value[i] * cnt)
        
        dp = [0 for _ in range(W + 1)]
        size = len(weight_new)
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight_new[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight_new[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
                    
        return dp[W]