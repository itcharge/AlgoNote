# [0474. 一和零](https://leetcode.cn/problems/ones-and-zeroes/)

- 标签：数组、字符串、动态规划
- 难度：中等

## 题目链接

- [0474. 一和零 - 力扣](https://leetcode.cn/problems/ones-and-zeroes/)

## 题目大意

**描述**：给定一个二进制字符串数组 $strs$，以及两个整数 $m$ 和 $n$。

**要求**：找出并返回 $strs$ 的最大子集的大小，该子集中最多有 $m$ 个 $0$ 和 $n$ 个 $1$。

**说明**：

- 如果 $x$ 的所有元素也是 $y$ 的元素，集合 $x$ 是集合 $y$ 的子集。
- $1 \le strs.length \le 600$。
- $1 \le strs[i].length \le 100$。
- $strs[i]$ 仅由 `'0'` 和 `'1'` 组成。
- $1 \le m, n \le 100$。

**示例**：

- 示例 1：

```python
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3。
```

- 示例 2：

```python
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2。
```

## 解题思路

### 思路 1：动态规划

这道题可以转换为「二维 0-1 背包问题」来做。

把 $0$ 的个数和 $1$ 的个数视作一个二维背包的容量。每一个字符串都当做是一件物品，其成本为字符串中 $1$ 的数量和 $0$ 的数量，每个字符串的价值为 $1$。

###### 1. 划分阶段

按照物品的序号、当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：最多有 $i$ 个 $0$ 和 $j$ 个 $1$ 的字符串 $strs$ 的最大子集的大小。

###### 3. 状态转移方程

填满最多由 $i$ 个 $0$ 和 $j$ 个 $1$ 构成的二维背包的最多物品数为下面两种情况中的最大值：

- 使用之前字符串填满容量为 $i - zero\underline{\hspace{0.5em}}num$、$j - one\underline{\hspace{0.5em}}num$ 的背包的物品数 + 当前字符串价值
- 选择之前字符串填满容量为 $i$、$j$ 的物品数。

则状态转移方程为：$dp[i][j] = max(dp[i][j], dp[i - zero\underline{\hspace{0.5em}}num][j - one\underline{\hspace{0.5em}}num] + 1)$。

###### 4. 初始条件

- 无论有多少个 $0$，多少个 $1$，只要不选 $0$，也不选 $1$，则最大子集的大小为 $0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][j]$ 表示为：最多有 $i$ 个 $0$ 和 $j$ 个 $1$ 的字符串 $strs$ 的最大子集的大小。所以最终结果为 $dp[m][n]$。

### 思路 1：代码

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for str in strs:
            one_num = 0
            zero_num = 0
            for ch in str:
                if ch == '0':
                    zero_num += 1
                else:
                    one_num += 1
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)

        return dp[m][n]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(l \times m \times n)$，其中 $l$ 为字符串 $strs$ 的长度。
- **空间复杂度**：$O(m \times n)$。

