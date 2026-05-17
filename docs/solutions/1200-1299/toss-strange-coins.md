# [1230. 抛掷硬币](https://leetcode.cn/problems/toss-strange-coins/)

- 标签：数学、动态规划、概率与统计
- 难度：中等

## 题目链接

- [1230. 抛掷硬币 - 力扣](https://leetcode.cn/problems/toss-strange-coins/)

## 题目大意

**描述**：有一些不规则的硬币。给定一个数组 $prob$，其中 $prob[i]$ 表示第 $i$ 枚硬币正面朝上的概率。给定一个整数 $target$。

**要求**：同时抛掷所有硬币，计算恰好有 $target$ 枚硬币正面朝上的概率。

**说明**：

- $1 \le prob.length \le 1000$。
- $0 \le prob[i] \le 1$。
- $0 \le target \le prob.length$。

**示例**：

- 示例 1：

```python
输入：prob = [0.4], target = 1
输出：0.40000
```

- 示例 2：

```python
输入：prob = [0.5,0.5,0.5], target = 0
输出：0.12500
解释：三枚硬币全是反面朝上的概率为 0.5×0.5×0.5=0.125。
```

## 解题思路

### 思路 1：动态规划

#### 1. 阶段划分

依次处理每枚硬币。对第 $i$ 枚硬币，考虑它正面向上的状态（正面或反面），然后更新概率分布。这和"背包问题"非常相似。

#### 2. 定义状态

定义 $dp[j]$ 表示处理到当前硬币时，恰好有 $j$ 枚硬币正面朝上的概率。

#### 3. 状态转移方程

考虑第 $i$ 枚硬币（正面概率为 $p$）：

- 它正面朝上：$dp'[j] += dp[j-1] \times p$（之前有 $j-1$ 枚正面，这一枚也正面）。
- 它反面朝上：$dp'[j] += dp[j] \times (1-p)$（之前有 $j$ 枚正面，这一枚反面）。

所以：

$$dp'[j] = dp[j] \times (1-p) + dp[j-1] \times p$$

#### 4. 初始条件

- $dp[0] = 1$（没有处理任何硬币时，$0$ 枚正面的概率为 $1$）。
- 其他 $dp[j] = 0$。

#### 5. 最终结果

$dp[target]$。

#### 6. 空间优化

可以用一维数组从后向前更新（类似 0-1 背包）：

```python
for j in range(min(i, target), 0, -1):
    dp[j] = dp[j] * (1-p) + dp[j-1] * p
dp[0] *= (1-p)
```

#### 7. 结合示例走一遍

$prob = [0.5, 0.5, 0.5], target = 0$

```
初始化: dp = [1]

第 0 枚硬币 (p=0.5):
  dp[1] = dp[1]*0.5 + dp[0]*0.5 = 0 + 1*0.5 = 0.5
  dp[0] = dp[0]*0.5 = 1*0.5 = 0.5
  → dp = [0.5, 0.5]

第 1 枚硬币 (p=0.5):
  dp[2] = dp[2]*0.5 + dp[1]*0.5 = 0 + 0.5*0.5 = 0.25
  dp[1] = dp[1]*0.5 + dp[0]*0.5 = 0.5*0.5 + 0.5*0.5 = 0.5
  dp[0] = dp[0]*0.5 = 0.5*0.5 = 0.25
  → dp = [0.25, 0.5, 0.25]

第 2 枚硬币 (p=0.5):
  dp[3] = dp[3]*0.5 + dp[2]*0.5 = 0 + 0.25*0.5 = 0.125
  dp[2] = dp[2]*0.5 + dp[1]*0.5 = 0.25*0.5 + 0.5*0.5 = 0.375
  dp[1] = dp[1]*0.5 + dp[0]*0.5 = 0.5*0.5 + 0.25*0.5 = 0.375
  dp[0] = dp[0]*0.5 = 0.25*0.5 = 0.125
  → dp = [0.125, 0.375, 0.375, 0.125]
```

$dp[0] = 0.125$。

### 思路 1：代码

```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [0.0] * (target + 1)
        dp[0] = 1.0

        for p in prob:
            # 从后向前更新，避免覆盖
            for j in range(min(target, n), 0, -1):
                dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
            dp[0] *= (1 - p)

        return dp[target]
```

注意：内层循环的上界目前写作 `min(target, n)`，但在遍历过程中应该限制为实际已经处理的硬币数量。更准确的写法是用一个计数器追踪已处理的硬币数。上面的写法在 $target \le n$ 时能用，但为了保险可以写成：

```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0.0] * (target + 1)
        dp[0] = 1.0
        for p in prob:
            # 从 min(target, 已处理硬币数) 向下遍历
            for j in range(target, 0, -1):
                dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
            dp[0] *= (1 - p)
        return dp[target]
```

因为 $j$ 从 $target$ 到 $1$，$dp[j-1]$ 引用的是上一轮的值，不会被覆盖。这更简洁。

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times target)$，其中 $n$ 是硬币数量。
- **空间复杂度**：$O(target)$，滚动数组优化后的空间。
