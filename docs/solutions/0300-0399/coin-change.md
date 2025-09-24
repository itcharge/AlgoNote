# [0322. 零钱兑换](https://leetcode.cn/problems/coin-change/)

- 标签：广度优先搜索、数组、动态规划
- 难度：中等

## 题目链接

- [0322. 零钱兑换 - 力扣](https://leetcode.cn/problems/coin-change/)

## 题目大意

**描述**：给定代表不同面额的硬币数组 $coins$ 和一个总金额 $amount$。

**要求**：求出凑成总金额所需的最少的硬币个数。如果无法凑出，则返回 $-1$。

**说明**：

- $1 \le coins.length \le 12$。
- $1 \le coins[i] \le 2^{31} - 1$。
- $0 \le amount \le 10^4$。

**示例**：

- 示例 1：

```python
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```

- 示例 2：

```python
输入：coins = [2], amount = 3
输出：-1
```

## 解题思路

### 思路 1：广度优先搜索

我们可以从 $amount$ 开始，每次从 $coins$ 的硬币中选中 $1$ 枚硬币，并记录当前挑选硬币的次数。则最快减到 $0$ 的次数就是凑成总金额所需的最少的硬币个数。这道题就变成了从 $amount$ 减到 $0$ 的最短路径问题。我们可以用广度优先搜索的方法来做。

1. 定义 $visited$ 为标记已访问值的集合变量，$queue$ 为存放值的队列。
2. 将 $amount$ 状态标记为访问，并将其加入队列 $queue$。
3. 令当前步数加 $1$，然后将当前队列中的所有值依次出队，并遍历硬币数组：
   1. 如果当前值等于当前硬币值，则说明当前硬币刚好能凑成当前值，则直接返回当前次数。
   2. 如果当前值大于当前硬币值，并且当前值减去当前硬币值的差值没有出现在已访问集合 $visited$ 中，则将差值添加到队列和访问集合中。

4. 重复执行第 $3$ 步，直到队列为空。
5. 如果队列为空，也未能减到 $0$，则返回 $-1$。

### 思路 1：代码

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set([amount])
        queue = collections.deque([amount])

        step = 0
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for coin in coins:
                    if cur == coin:
                        step += 1
                        return step
                    elif cur > coin and cur - coin not in visited:
                        queue.append(cur - coin)
                        visited.add(cur - coin)
            
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(amount \times size)$。其中 $amount$ 表示总金额，$size$ 表示硬币的种类数。
- **空间复杂度**：$O(amount)$。

### 思路 2：完全背包问题

这道题可以转换为：有 $n$ 种不同的硬币，$coins[i]$ 表示第 $i$ 种硬币的面额，每种硬币可以无限次使用。请问恰好凑成总金额为 $amount$ 的背包，最少需要多少硬币？

与普通完全背包问题不同的是，这里求解的是最少硬币数量。我们可以改变一下「状态定义」和「状态转移方程」。

###### 1. 阶段划分

按照当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[c]$ 表示为：凑成总金额为 $c$ 的最少硬币数量。

###### 3. 状态转移方程

$dp[c] = \begin{cases} dp[c] & c < coins[i - 1] \cr min \lbrace dp[c], dp[c - coins[i - 1]]  + 1 \rbrace & c \ge coins[i - 1] \end{cases}$

1. 当 $c < coins[i - 1]$ 时：
   1. 不使用第 $i - 1$ 枚硬币，只使用前 $i - 1$ 枚硬币凑成金额 $w$ 的最少硬币数量，即 $dp[c]$。
2. 当 $c \ge coins[i - 1]$ 时，取下面两种情况中的较小值：
   1. 不使用第 $i - 1$ 枚硬币，只使用前 $i - 1$ 枚硬币凑成金额 $w$ 的最少硬币数量，即 $dp[c]$。
   2. 凑成金额 $c - coins[i - 1]$ 的最少硬币数量，再加上当前硬币的数量 $1$，即 $dp[c - coins[i - 1]]  + 1$。

###### 4. 初始条件

- 凑成总金额为 $0$ 的最少硬币数量为 $0$，即 $dp[0] = 0$。
- 默认情况下，在不使用硬币时，都不能恰好凑成总金额为 $w$ ，此时将状态值设置为一个极大值（比如 $n + 1$），表示无法凑成。

###### 5. 最终结果

根据我们之前定义的状态，$dp[c]$ 表示为：凑成总金额为 $c$ 的最少硬币数量。则最终结果为 $dp[amount]$。

1. 如果 $dp[amount] \ne amount + 1$，则说明： $dp[amount]$ 为凑成金额 $amount$ 的最少硬币数量，则返回 $dp[amount]$。
2. 如果 $dp[amount] = amount + 1$，则说明：无法凑成金额 $amount$，则返回 $-1$。

### 思路 2：代码

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        size = len(coins)
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0

        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for c in range(coins[i - 1], amount + 1):
                dp[c] = min(dp[c], dp[c - coins[i - 1]] + 1)
        
        if dp[amount] != amount + 1:
            return dp[amount]
        return -1
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(amount \times size)$。其中 $amount$ 表示总金额，$size$ 表示硬币的种类数。
- **空间复杂度**：$O(amount)$。