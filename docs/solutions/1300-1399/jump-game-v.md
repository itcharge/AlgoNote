# [1340. 跳跃游戏 V](https://leetcode.cn/problems/jump-game-v/)

- 标签：数组、动态规划、排序
- 难度：困难

## 题目链接

- [1340. 跳跃游戏 V - 力扣](https://leetcode.cn/problems/jump-game-v/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个整数 $d$。你可以从 $i$ 跳到 $i+x$，其中 $-d \le x \le d$ 且路径上所有 $arr[j] < arr[i]$。

**要求**：返回最多能访问多少个下标（从某个下标出发，每一步只能跳到更高的柱子...不对，只能跳到更矮的柱子）。

实际上是：你可以从任何下标开始，每次只能跳到比当前值严格小的相邻位置（在 $d$ 范围内），每个位置只能访问一次。求能访问的最多下标数。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/02/meta-chart.jpeg)

```python
输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
输出：4
解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。
注意，如果你从下标 6 开始，你只能跳到下标 7 处。你不能跳到下标 5 处因为 13 > 9 。你也不能跳到下标 4 处，因为下标 5 在下标 4 和 6 之间且 13 > 9 。
类似的，你不能从下标 3 处跳到下标 2 或者下标 1 处。
```

- 示例 2：

```python
输入：arr = [3,3,3,3,3], d = 3
输出：1
解释：你可以从任意下标处开始且你永远无法跳到任何其他坐标。
```


## 解题思路

### 思路 1：记忆化搜索

#### 1. 核心思想

按值从小到大排序，值大的位置可以跳到值小的相邻位置。定义 $dp[i]$ 为从 $i$ 出发能访问的最多下标数。

对 $i$ 在 $d$ 范围内向左/右找比 $arr[i]$ 严格小的位置 $j$，$dp[i] = \max(dp[j] + 1)$。

也可以直接用记忆化搜索（DFS + 缓存）。

#### 2. 具体步骤

**第 1 步**：定义 $dfs(i)$ 返回从 $i$ 出发的最大访问数。

**第 2 步**：向左右在 $d$ 范围内扩展，遇到第一个 $\ge arr[i]$ 的柱子则停止。

### 思路 1：代码

```python
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            res = 1
            # 向右
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
            # 向左
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
            return res

        return max(dfs(i) for i in range(n))
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(nd)$。
- **空间复杂度**：$O(n)$。
