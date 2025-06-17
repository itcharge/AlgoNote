class Solution:
    def mixedPackMethod1(self, weight: [int], value: [int], count: [int], W: int):
        weight_new, value_new, count_new = [], [], []
        
        # 二进制优化
        for i in range(len(weight)):
            cnt = count[i]
            # 多重背包问题，转为 0-1 背包问题
            if cnt > 0:
                k = 1
                while k <= cnt:
                    cnt -= k
                    weight_new.append(weight[i] * k)
                    value_new.append(value[i] * k)
                    count_new.append(1)
                    k *= 2
                if cnt > 0:
                    weight_new.append(weight[i] * cnt)
                    value_new.append(value[i] * cnt)
                    count_new.append(1)
            # 0-1 背包问题，直接添加
            elif cnt == -1:
                weight_new.append(weight[i])
                value_new.append(value[i])
                count_new.append(1)
            # 完全背包问题，标记并添加
            else:
                weight_new.append(weight[i])
                value_new.append(value[i])
                count_new.append(0)
                
        dp = [0 for _ in range(W + 1)]
        size = len(weight_new)
    
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 0-1 背包问题
            if count_new[i - 1] == 1:
                # 逆序枚举背包装载重量（避免状态值错误）
                for w in range(W, weight_new[i - 1] - 1, -1):
                    # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight_new[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                    dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
            # 完全背包问题
            else:
                # 正序枚举背包装载重量
                for w in range(weight_new[i - 1], W + 1):
                    # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                    dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
                    
        return dp[W]