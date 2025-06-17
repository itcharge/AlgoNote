# [0873. 最长的斐波那契子序列的长度](https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/)

- 标签：数组、哈希表、动态规划
- 难度：中等

## 题目链接

- [0873. 最长的斐波那契子序列的长度 - 力扣](https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/)

## 题目大意

**描述**：给定一个严格递增的正整数数组 $arr$。

**要求**：从数组 $arr$ 中找出最长的斐波那契式的子序列的长度。如果不存斐波那契式的子序列，则返回 0。

**说明**：

- **斐波那契式序列**：如果序列 $X_1, X_2, ..., X_n$ 满足：

  - $n \ge 3$；
  - 对于所有 $i + 2 \le n$，都有 $X_i + X_{i+1} = X_{i+2}$。

  则称该序列为斐波那契式序列。

- **斐波那契式子序列**：从序列 $A$ 中挑选若干元素组成子序列，并且子序列满足斐波那契式序列，则称该序列为斐波那契式子序列。例如：$A = [3, 4, 5, 6, 7, 8]$。则 $[3, 5, 8]$ 是 $A$ 的一个斐波那契式子序列。

- $3 \le arr.length \le 1000$。

- $1 \le arr[i] < arr[i + 1] \le 10^9$。

**示例**：

- 示例 1：

```python
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8]。
```

- 示例 2：

```python
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18]。
```

## 解题思路

### 思路 1： 暴力枚举（超时）

假设 $arr[i]$、$arr[j]$、$arr[k]$ 是序列 $arr$ 中的 $3$ 个元素，且满足关系：$arr[i] + arr[j] == arr[k]$，则 $arr[i]$、$arr[j]$、$arr[k]$ 就构成了 $arr$ 的一个斐波那契式子序列。

通过  $arr[i]$、$arr[j]$，我们可以确定下一个斐波那契式子序列元素的值为 $arr[i] + arr[j]$。

因为给定的数组是严格递增的，所以对于一个斐波那契式子序列，如果确定了 $arr[i]$、$arr[j]$，则可以顺着 $arr$ 序列，从第 $j + 1$ 的元素开始，查找值为 $arr[i] + arr[j]$ 的元素 。找到 $arr[i] + arr[j]$ 之后，然后再顺着查找子序列的下一个元素。

简单来说，就是确定了 $arr[i]$、$arr[j]$，就能尽可能的得到一个长的斐波那契式子序列，此时我们记录下子序列长度。然后对于不同的  $arr[i]$、$arr[j]$，统计不同的斐波那契式子序列的长度。

最后将这些长度进行比较，其中最长的长度就是答案。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 为数组 $arr$ 的元素个数。
- **空间复杂度**：$O(1)$。

### 思路 2：哈希表

对于 $arr[i]$、$arr[j]$，要查找的元素 $arr[i] + arr[j]$ 是否在 $arr$ 中，我们可以预先建立一个反向的哈希表。键值对关系为 $value : idx$，这样就能在 $O(1)$ 的时间复杂度通过 $arr[i] + arr[j]$ 的值查找到对应的 $arr[k]$，而不用像原先一样线性查找 $arr[k]$ 了。

### 思路 2：代码

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

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组 $arr$ 的元素个数。
- **空间复杂度**：$O(n)$。

### 思路 3：动态规划 + 哈希表

###### 1. 划分阶段

按照斐波那契式子序列相邻两项的结尾位置进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][j]$ 表示为：以 $arr[i]$、$arr[j]$ 为结尾的斐波那契式子序列的最大长度。

###### 3. 状态转移方程

以 $arr[j]$、$arr[k]$ 结尾的斐波那契式子序列的最大长度 = 满足 $arr[i] + arr[j] = arr[k]$ 条件下，以 $arr[i]$、$arr[j]$ 结尾的斐波那契式子序列的最大长度加 $1$。即状态转移方程为：$dp[j][k] = max_{(A[i] + A[j] = A[k], i < j < k)}(dp[i][j] + 1)$。

###### 4. 初始条件

默认状态下，数组中任意相邻两项元素都可以作为长度为 $2$ 的斐波那契式子序列，即 $dp[i][j] = 2$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][j]$ 表示为：以 $arr[i]$、$arr[j]$ 为结尾的斐波那契式子序列的最大长度。那为了计算出最大的最长递增子序列长度，则需要在进行状态转移时，求出最大值 $ans$ 即为最终结果。

因为题目定义中，斐波那契式中 $n \ge 3$，所以只有当 $ans \ge 3$ 时，返回 $ans$。如果 $ans < 3$，则返回 $0$。

> **注意**：在进行状态转移的同时，我们应和「思路 2：哈希表」一样采用哈希表优化的方式来提高效率，降低算法的时间复杂度。

### 思路 3：代码

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        
        dp = [[0 for _ in range(size)] for _ in range(size)]
        ans = 0

        # 初始化 dp
        for i in range(size):
            for j in range(i + 1, size):
                dp[i][j] = 2

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

        if ans >= 3:
            return ans
        return 0
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组 $arr$ 的元素个数。
- **空间复杂度**：$O(n)$。

