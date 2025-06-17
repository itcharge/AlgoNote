class Solution:
    # 1. 求恰好装满背包的最大价值
    
    # 0-1 背包问题 求恰好装满背包的最大价值
    def zeroOnePackJustFillUp(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [float('-inf') for _ in range(W + 1)]
        dp[0] = 0
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
        
        if dp[W] == float('-inf'):
            return -1
        return dp[W]
    
    # 完全背包问题 求恰好装满背包的最大价值
    def completePackJustFillUp(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [float('-inf') for _ in range(W + 1)]
        dp[0] = 0
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                
        if dp[W] == float('-inf'):
            return -1
        return dp[W]
    
    
    # 2. 求方案总数
    
    # 0-1 背包问题 求方案总数
    def zeroOnePackNumbers(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        dp[0] = 1
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量
            for w in range(W, weight[i - 1] - 1, -1):
                # dp[w] = 前 i - 1 件物品装入载重为 w 的背包中的方案数 + 前 i 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 件物品的方案数
                dp[w] = dp[w] + dp[w - weight[i - 1]]
                
        return dp[W]
    
    # 完全背包问题求方案总数
    def completePackNumbers(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        dp[0]  = 1
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] = 前 i - 1 种物品装入载重为 w 的背包中的方案数 + 前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品的方案数
                dp[w] = dp[w] + dp[w - weight[i - 1]]
                
        return dp[W]
    
    
    # 3. 求最优方案数
    
    # 0-1 背包问题 求最优方案数 思路 1
    def zeroOnePackMaxProfitNumbers1(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        op = [[1 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                    op[i][w] = op[i - 1][w]
                else:
                    # 选择第 i - 1 件物品获得价值更高
                    if dp[i - 1][w] < dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w - weight[i - 1]] + value[i - 1]
                        # 在之前方案基础上添加了第 i - 1 件物品，因此方案数量不变
                        op[i][w] = op[i - 1][w - weight[i - 1]]
                    # 两种方式获得价格相等
                    elif dp[i - 1][w] == dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w]
                        # 方案数 = 不使用第 i - 1 件物品的方案数 + 使用第 i - 1 件物品的方案数
                        op[i][w] = op[i - 1][w] + op[i - 1][w - weight[i - 1]]
                    # 不选择第 i - 1 件物品获得价值最高
                    else:
                        dp[i][w] = dp[i - 1][w]
                        # 不选择第 i - 1 件物品，与之前方案数相等
                        op[i][w] = op[i - 1][w]
                        
        return op[size][W]
    
    # 0-1 背包问题求最优方案数 思路 2
    def zeroOnePackMaxProfitNumbers2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        op = [1 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W, weight[i - 1] - 1, -1):
                # 选择第 i - 1 件物品获得价值更高
                if dp[w] < dp[w - weight[i - 1]] + value[i - 1]:
                    dp[w] = dp[w - weight[i - 1]] + value[i - 1]
                    # 在之前方案基础上添加了第 i - 1 件物品，因此方案数量不变
                    op[w] = op[w - weight[i - 1]]
                # 两种方式获得价格相等
                elif dp[w] == dp[w - weight[i - 1]] + value[i - 1]:
                    # 方案数 = 不使用第 i - 1 件物品的方案数 + 使用第 i - 1 件物品的方案数
                    op[w] = op[w] + op[w - weight[i - 1]]
                        
        return op[W]

    # 完全背包问题求最优方案数 思路 1
    def completePackMaxProfitNumbers1(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        op = [[1 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                    op[i][w] = op[i - 1][w]
                else:
                    # 选择第 i - 1 件物品获得价值更高
                    if dp[i - 1][w] < dp[i][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i][w - weight[i - 1]] + value[i - 1]
                        # 在之前方案基础上添加了 1 件第 i - 1 种物品，因此方案数量不变
                        op[i][w] = op[i][w - weight[i - 1]]
                    # 两种方式获得价格相等
                    elif dp[i - 1][w] == dp[i][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w]
                        # 方案数 = 不使用第 i - 1 种物品的方案数 + 使用 1 件第 i - 1 种物品的方案数
                        op[i][w] = op[i - 1][w] + op[i][w - weight[i - 1]]
                    # 不选择第 i - 1 件物品获得价值最高
                    else:
                        dp[i][w] = dp[i - 1][w]
                        # 不选择第 i - 1 种物品，与之前方案数相等
                        op[i][w] = op[i - 1][w]
                    
        return dp[size][W]
    
    # 完全背包问题求最优方案数 思路 2
    def completePackMaxProfitNumbers2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        op = [1 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # 选择第 i - 1 件物品获得价值更高
                if dp[w] < dp[w - weight[i - 1]] + value[i - 1]:
                    dp[w] = dp[w - weight[i - 1]] + value[i - 1]
                    # 在之前方案基础上添加了 1 件第 i - 1 种物品，因此方案数量不变
                    op[w] = op[w - weight[i - 1]]
                # 两种方式获得价格相等
                elif dp[w] == dp[w - weight[i - 1]] + value[i - 1]:
                    # 方案数 = 不使用第 i - 1 种物品的方案数 + 使用 1 件第 i - 1 种物品的方案数
                    op[w] = op[w] + op[w - weight[i - 1]]
                    
        return dp[size][W]
    
    
    # 4. 求具体方案
    
    # 0-1 背包问题求具体方案
    def zeroOnePackPrintPath(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        path = [[False for _ in range(W + 1)] for _ in range(size + 1)]
    
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                    path[i][w] = False
                else:
                    # 选择第 i - 1 件物品获得价值更高
                    if dp[i - 1][w] < dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w - weight[i - 1]] + value[i - 1]
                        # 取状态转移式第二项：在之前方案基础上添加了第 i - 1 件物品
                        path[i][w] = True
                    # 两种方式获得价格相等
                    elif dp[i - 1][w] == dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w]
                        # 取状态转移式第二项：尽量使用第 i - 1 件物品
                        path[i][w] = True
                    # 不选择第 i - 1 件物品获得价值最高
                    else:
                        dp[i][w] = dp[i - 1][w]
                        # 取状态转移式第一项：不选择第 i - 1 件物品
                        path[i][w] = False
                        
        res = []
        i, w = size, W
        while i >= 1 and w >= 0:
            if path[i][w]:
                res.append(str(i - 1))
                w -= weight[i - 1]
            i -= 1
            
        return " ".join(res[::-1])
    
    # 0-1 背包问题求具体方案，要求最小序输出
    def zeroOnePackPrintPathMinOrder(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        path = [[False for _ in range(W + 1)] for _ in range(size + 1)]
        
        weight.reverse()
        value.reverse()
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                    path[i][w] = False
                else:
                    # 选择第 i - 1 件物品获得价值更高
                    if dp[i - 1][w] < dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w - weight[i - 1]] + value[i - 1]
                        # 取状态转移式第二项：在之前方案基础上添加了第 i - 1 件物品
                        path[i][w] = True
                    # 两种方式获得价格相等
                    elif dp[i - 1][w] == dp[i - 1][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i - 1][w]
                        # 取状态转移式第二项：尽量使用第 i - 1 件物品
                        path[i][w] = True
                    # 不选择第 i - 1 件物品获得价值最高
                    else:
                        dp[i][w] = dp[i - 1][w]
                        # 取状态转移式第一项：不选择第 i - 1 件物品
                        path[i][w] = False
                        
        res = []
        i, w = size, W
        while i >= 1 and w >= 0:
            if path[i][w]:
                res.append(str(size - i))
                w -= weight[i - 1]
            i -= 1
            
        return " ".join(res)