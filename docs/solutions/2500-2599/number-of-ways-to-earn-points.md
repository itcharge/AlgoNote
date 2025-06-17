# [2585. 获得分数的方法数](https://leetcode.cn/problems/number-of-ways-to-earn-points/)

- 标签：数组、动态规划
- 难度：困难

## 题目链接

- [2585. 获得分数的方法数 - 力扣](https://leetcode.cn/problems/number-of-ways-to-earn-points/)

## 题目大意

**描述**：考试中有 $n$ 种类型的题目。给定一个整数 $target$ 和一个下标从 $0$ 开始的二维整数数组 $types$，其中 $types[i] = [count_i, marks_i]$ 表示第 $i$ 种类型的题目有 $count_i$ 道，每道题目对应 $marks_i$ 分。

**要求**：返回你在考试中恰好得到 $target$ 分的方法数。由于答案可能很大，结果需要对 $10^9 + 7$ 取余。

**说明**：

- 同类型题目无法区分。比如说，如果有 $3$ 道同类型题目，那么解答第 $1$ 和第 $2$ 道题目与解答第 $1$ 和第 $3$ 道题目或者第 $2$ 和第 $3$ 道题目是相同的。
- $1 \le target \le 1000$。
- $n == types.length$。
- $1 \le n \le 50$。
- $types[i].length == 2$。
- $1 \le counti, marksi \le 50$。

**示例**：

- 示例 1：

```python
输入：target = 6, types = [[6,1],[3,2],[2,3]]
输出：7
解释：要获得 6 分，你可以选择以下七种方法之一：
- 解决 6 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 + 1 = 6
- 解决 4 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 1 + 2 = 6
- 解决 2 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 1 + 2 + 2 = 6
- 解决 3 道第 0 种类型的题目和 1 道第 2 种类型的题目：1 + 1 + 1 + 3 = 6
- 解决 1 道第 0 种类型的题目、1 道第 1 种类型的题目和 1 道第 2 种类型的题目：1 + 2 + 3 = 6
- 解决 3 道第 1 种类型的题目：2 + 2 + 2 = 6
- 解决 2 道第 2 种类型的题目：3 + 3 = 6
```

- 示例 2：

```python
输入：target = 5, types = [[50,1],[50,2],[50,5]]
输出：4
解释：要获得 5 分，你可以选择以下四种方法之一：
- 解决 5 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 = 5
- 解决 3 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 2 = 5
- 解决 1 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 2 + 2 = 5
- 解决 1 道第 2 种类型的题目：5
```

## 解题思路

### 思路 1：动态规划

###### 1. 划分阶段

按照进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][w]$ 表示为：前 $i$ 种题目恰好组成 $w$ 分的方案数。

###### 3. 状态转移方程

前 $i$ 种题目恰好组成 $w$ 分的方案数，等于前 $i - 1$ 种问题恰好组成 $w - k \times marks_i$ 分的方案数总和，即状态转移方程为：$dp[i][w] = \sum_{k = 0} dp[i - 1][w - k \times marks_i]$。

###### 4. 初始条件

- 前 $0$ 种题目恰好组成 $0$ 分的方案数为 $1$。

###### 5. 最终结果

根据我们之前定义的状态， $dp[i][w]$ 表示为：前 $i$ 种题目恰好组成 $w$ 分的方案数。 所以最终结果为 $dp[size][target]$。

### 思路 1：代码

```python
class Solution:    
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        size = len(types)
        group_count = [types[i][0] for i in range(len(types))]
        weight = [[(types[i][1] * k) for k in range(types[i][0] + 1)] for i in range(len(types))]
        mod = 1000000007
            
        dp = [[0 for _ in range(target + 1)] for _ in range(size + 1)]
        dp[0][0] = 1
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(target + 1):
                # 枚举第 i 组物品能取个数
                dp[i][w] = dp[i - 1][w]
                for k in range(1, group_count[i - 1] + 1):
                    if w >= weight[i - 1][k]:
                        dp[i][w] += dp[i - 1][w - weight[i - 1][k]]
                        dp[i][w] %= mod
        
        return dp[size][target]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times target \times m)$，其中 $n$ 为题目种类数，$target$ 为目标分数，$m$ 为每种题目的最大分数。
- **空间复杂度**：$O(n \times target)$。

