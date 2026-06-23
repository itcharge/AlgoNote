# [1434. 每个人戴不同帽子的方案数](https://leetcode.cn/problems/number-of-ways-to-wear-different-hats-to-each-other/)

- 标签：位运算、数组、动态规划、状态压缩
- 难度：困难

## 题目链接

- [1434. 每个人戴不同帽子的方案数 - 力扣](https://leetcode.cn/problems/number-of-ways-to-wear-different-hats-to-each-other/)

## 题目大意

**描述**：给定一个 $n \times ?$ 的二维列表 $hats$，$hats[i]$ 是第 $i$ 个人喜欢的帽子列表。每顶帽子只能给一个人，每个人只能戴一顶自己最喜欢的帽子。

**要求**：返回每个人都戴到喜欢帽子的方案数。结果对 $10^9 + 7$ 取模。

**说明**：
- $1 \le n \le 10$。
- $1 \le hats[i].length \le 40$。
- $1 \le hat.id \le 40$。

**示例**：

- 示例 1：

```python
输入：hats = [[3,4],[4,5],[5]]
输出：1
解释：给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
```

- 示例 2：

```python
输入：hats = [[3,5,1],[3,5]]
输出：4
解释：总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)
```

## 解题思路

### 思路 1：状压 DP

#### 1. 核心思想

人数 $n \le 10$，可以用状态压缩表示哪些人已经分配了帽子。帽子数量 $m \le 40$。

按帽子编号从小到大的顺序处理：对于每顶帽子，选择一个人分配（或不分给任何人）。

#### 2. 阶段划分

按帽子编号 $h$ 划分阶段，从 $1$ 到 $max\_hat$。

#### 3. 定义状态

$dp[mask]$ 表示当前帽子分配的状态，$mask$ 的第 $i$ 位为 $1$ 表示第 $i$ 个人已分配到帽子。

初始化 $dp[0] = 1$。

#### 4. 状态转移方程

对于第 $h$ 顶帽子，逆序遍历所有 $mask$：
- 第 $h$ 顶帽子不分给任何人：$dp[mask]$ 不变（等效于跳过这顶帽子，即 $dp$ 数组天然的滚动更新）。
- 第 $h$ 顶帽子分给第 $i$ 个人：如果 $h$ 在 $hats[i]$ 中且 $mask$ 的第 $i$ 位是 $0$：

$$dp[mask \mid (1 << i)] += dp[mask]$$

更准确地说，用滚动数组实现时，对于每个 $h$，遍历 $mask$ 从大到小，更新。

#### 5. 最终结果

$dp[(1<<n)-1]$。

#### 6. 举例说明

以 $n=2$，$hats = [[1,2,3],[2,3]]$ 为例：

$dp[0] = 1$
帽子 1：只能给第 0 人 → $dp[01] += dp[00] = 1$
帽子 2：可给第 0 人或第 1 人
- $dp[01] += dp[00]$（给第 0 人），$dp[10] += dp[00]$（给第 1 人）
帽子 3：类似
...

最终 $dp[11]$ 即为答案。

### 思路 1：代码

```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        max_hat = 40

        # hat_to_person[hat] = 喜欢该帽子的人列表
        hat_to_person = [[] for _ in range(max_hat + 1)]
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_person[hat].append(person)

        total_states = 1 << n
        dp = [0] * total_states
        dp[0] = 1

        # 遍历每顶帽子
        for hat in range(1, max_hat + 1):
            # 逆序遍历所有状态（滚动数组）
            for mask in range(total_states - 1, -1, -1):
                for person in hat_to_person[hat]:
                    if not (mask >> person) & 1:
                        new_mask = mask | (1 << person)
                        dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

        return dp[total_states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times 2^n \times n)$，$m=40, n\le10$，可行。
- **空间复杂度**：$O(2^n)$。
