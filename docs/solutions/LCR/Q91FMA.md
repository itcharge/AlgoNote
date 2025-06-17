# [LCR 093. 最长的斐波那契子序列的长度](https://leetcode.cn/problems/Q91FMA/)

- 标签：数组、哈希表、动态规划
- 难度：中等

## 题目链接

- [LCR 093. 最长的斐波那契子序列的长度 - 力扣](https://leetcode.cn/problems/Q91FMA/)

## 题目大意

给定一个严格递增的正整数数组 `arr`。

要求：从 `arr` 中找出最长的斐波那契式的子序列的长度。如果不存斐波那契式的子序列，则返回 `0`。

- 斐波那契式序列：如果序列 $X_1, X_2, ..., X_n$ 满足：

    - $n \ge 3$；
    - 对于所有 $i + 2 \le n$，都有 $X_i + X_{i+1} = X_{i+2}$。

    则称该序列为斐波那契式序列。

- 斐波那契式子序列：从序列 `arr` 中挑选若干元素组成子序列，并且子序列满足斐波那契式序列，则称该序列为斐波那契式子序列。例如：`arr = [3, 4, 5, 6, 7, 8]`。则 `[3, 5, 8]` 是 `arr` 的一个斐波那契式子序列。

## 解题思路

我们先从最简单的暴力做法思考。

**1. 暴力做法：**

我们先来考虑暴力做法怎么做。

假设 `arr[i]`、`arr[j]`、`arr[k]` 是序列 `arr` 中的 3 个元素，且满足关系：`arr[i] + arr[j] == arr[k]`，则 `arr[i]`、`arr[j]`、`arr[k]` 就构成了 A 的一个斐波那契式子序列。

通过  `arr[i]`、`arr[j]`，我们可以确定下一个斐波那契式子序列元素的值为 `arr[i] + arr[j]`。

因为给定的数组是严格递增的，所以对于一个斐波那契式子序列，如果确定了 `arr[i]`、`arr[j]`，则可以顺着 `arr` 序列，从第 `j + 1` 的元素开始，查找值为 `arr[i] + arr[j]` 的元素 。找到 `arr[i] + arr[j]` 之后，然后在顺着查找子序列的下一个元素。

简单来说，就是确定了 `arr[i]`、`arr[j]`，就能尽可能的得到一个长的斐波那契式子序列，此时我们记录下子序列长度。然后对于不同的  `arr[i]`、`arr[j]`，统计不同的斐波那契式子序列的长度。将这些长度进行比较，其中最长的长度就是答案。

下面是暴力做法的代码：

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        for i in range(size):
            for j in range(i + 1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                k = j + 1
                while k < size:
                    if arr[temp_i] + arr[temp_j] == arr[k]:
                        temp_ans += 1
                        temp_i = temp_j
                        temp_j = k
                    k += 1
                if temp_ans > ans:
                    ans = temp_ans

        if ans > 0:
            return ans + 2
        else:
            return ans
```

毫无意外的，超出时间限制了。

那么我们怎么来优化呢？

**2. 使用哈希表优化做法：**

我们注意到：对于 `arr[i]`、`arr[j]`，要查找的元素 `arr[i] + arr[j]` 是否在 `arr` 中，我们可以预先建立一个反向的哈希表。键值对关系为 `value : idx`，这样就能在 `O(1)` 的时间复杂度通过 `arr[i] + arr[j]` 的值查找到对应的 `k` 值，而不用像原先一样线性查找 `arr[k]` 了。

使用哈希表优化之后的代码如下：

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        idx_map = dict()
        for idx, value in enumerate(arr):
            idx_map[value] = idx
        
        for i in range(size):
            for j in range(i + 1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                while arr[temp_i] + arr[temp_j] in idx_map:
                    temp_ans += 1
                    k = idx_map[arr[temp_i] + arr[temp_j]]
                    temp_i = temp_j
                    temp_j = k

                if temp_ans > ans:
                    ans = temp_ans

        if ans > 0:
            return ans + 2
        else:
            return ans
```

再次提交，通过了。

但是，这道题我们还可以用动态规划来做。

**3. 动态规划做法：**

这道题用动态规划来做，难点在于如何「定义状态」和「定义状态转移方程」。

- 定义状态：`dp[i][j]` 表示以 `arr[i]`、`arr[j]` 为结尾的斐波那契式子序列的最大长度。
- 定义状态转移方程：$dp[j][k] = max_{(arr[i] + arr[j] = arr[k], i < j < k)}(dp[i][j] + 1)$
    - 意思为：以 `arr[j]`、`arr[k]` 结尾的斐波那契式子序列的最大长度 = 满足 `arr[i] + arr[j] = arr[k]` 条件下，以 `arr[i]`、`arr[j]` 结尾的斐波那契式子序列的最大长度 + 1。

但是直接这样做其实跟 **1. 暴力解法** 一样仍会超时，所以我们依旧采用哈希表优化的方式来提高效率，降低算法的时间复杂度。

具体代码如下：

## 代码

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        # 初始化 dp
        dp = [[0 for _ in range(size)] for _ in range(size)]
        ans = 0
        idx_map = {}
        # 将 value : idx 映射为哈希表，这样可以快速通过 value 获取到 idx
        for idx, value in enumerate(arr):
            idx_map[value] = idx

        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] + arr[j] in idx_map:
                    # 获取 arr[i] + arr[j] 的 idx，即斐波那契式子序列下一项元素
                    k = idx_map[arr[i] + arr[j]]

                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    ans = max(ans, dp[j][k])

        if ans > 0:
            return ans + 2
        else:
            return ans
```

