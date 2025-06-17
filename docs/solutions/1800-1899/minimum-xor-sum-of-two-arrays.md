# [1879. 两个数组最小的异或值之和](https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/)

- 标签：位运算、数组、动态规划、状态压缩
- 难度：困难

## 题目链接

- [1879. 两个数组最小的异或值之和 - 力扣](https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/)

## 题目大意

**描述**：给定两个整数数组 $nums1$ 和 $nums2$，两个数组长度都为 $n$。

**要求**：将 $nums2$ 中的元素重新排列，使得两个数组的异或值之和最小。并返回重新排列之后的异或值之和。

**说明**：

- **两个数组的异或值之和**：$(nums1[0] \oplus nums2[0]) + (nums1[1] \oplus nums2[1]) + ... + (nums1[n - 1] \oplus nums2[n - 1])$（下标从 $0$ 开始）。
- 举个例子，$[1, 2, 3]$ 和 $[3,2,1]$ 的异或值之和 等于 $(1 \oplus 3) + (2 \oplus 2) + (3 \oplus 1) + (3 \oplus 1) = 2 + 0 + 2 = 4$。
- $n == nums1.length$。
- $n == nums2.length$。
- $1 \le n \le 14$。
- $0 \le nums1[i], nums2[i] \le 10^7$。

**示例**：

- 示例 1：

```python
输入：nums1 = [1,2], nums2 = [2,3]
输出：2
解释：将 nums2 重新排列得到 [3,2] 。
异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2。
```

- 示例 2：

```python
输入：nums1 = [1,0,3], nums2 = [5,3,4]
输出：8
解释：将 nums2 重新排列得到 [5,4,3] 。
异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8。
```

## 解题思路

### 思路 1：状态压缩 DP

由于数组 $nums2$ 可以重新排列，所以我们可以将数组 $nums1$ 中的元素顺序固定，然后将数组 $nums1$ 中第 $i$ 个元素与数组 $nums2$ 中所有还没被选择的元素进行组合，找到异或值之和最小的组合。

同时因为两个数组长度 $n$ 的大小范围只有 $[1, 14]$，所以我们可以采用「状态压缩」的方式来表示 $nums2$ 中当前元素的选择情况。

「状态压缩」指的是使用一个 $n$ 位的二进制数 $state$ 来表示排列中数的选取情况。

如果二进制数 $state$ 的第 $i$ 位为 $1$，说明数组 $nums2$ 第 $i$ 个元素在该状态中被选取。反之，如果该二进制的第 $i$ 位为 $0$，说明数组 $nums2$ 中第 $i$ 个元素在该状态中没有被选取。

举个例子：

1. $nums2 = \lbrace 1, 2, 3, 4 \rbrace$，$state = (1001)_2$，表示选择了第 $1$ 个元素和第 $4$ 个元素，也就是 $1$、$4$。
2. $nums2 = \lbrace 1, 2, 3, 4, 5, 6 \rbrace$，$state = (011010)_2$，表示选择了第 $2$ 个元素、第 $4$ 个元素、第 $5$ 个元素，也就是  $2$、$4$、$5$。

这样，我们就可以通过动态规划的方式来解决这道题。

###### 1. 划分阶段

按照数组 $nums$ 中元素选择情况进行阶段划分。

###### 2. 定义状态

定义当前数组 $nums2$ 中元素选择状态为 $state$，$state$ 对应选择的元素个数为 $count(state)$。

则可以定义状态 $dp[state]$ 表示为：当前数组 $nums2$ 中元素选择状态为 $state$，并且选择了 $nums1$ 中前 $count(state)$ 个元素的情况下，可以组成的最小异或值之和。

###### 3. 状态转移方程

对于当前状态 $dp[state]$，肯定是从比 $state$ 少选一个元素的状态中递推而来。我们可以枚举少选一个元素的状态，找到可以组成的异或值之和最小值，赋值给 $dp[state]$。

举个例子 $nums2 = \lbrace 1, 2, 3, 4 \rbrace$，$state = (1001)_2$，表示选择了第 $1$ 个元素和第 $4$ 个元素，也就是 $1$、$4$。那么 $state$ 只能从 $(1000)_2$ 和 $(0001)_2$ 这两个状态转移而来，我们只需要枚举这两种状态，并求出转移过来的异或值之和最小值。

即状态转移方程为：$dp[state] = min(dp[state], \quad dp[state \oplus (1 \text{ <}\text{< } i)] + (nums1[i] \oplus nums2[one\underline{\hspace{0.5em}}cnt - 1]))$，其中 $state$ 第 $i$ 位一定为 $1$，$one\underline{\hspace{0.5em}}cnt$ 为 $state$ 中 $1$ 的个数。

###### 4. 初始条件

- 既然是求最小值，不妨将所有状态初始为最大值。
- 未选择任何数时，异或值之和为 $0$，所以初始化 $dp[0] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[state]$ 表示为：当前数组 $nums2$ 中元素选择状态为 $state$，并且选择了 $nums1$ 中前 $count(state)$ 个元素的情况下，可以组成的最小异或值之和。 所以最终结果为 $dp[states - 1]$，其中 $states = 1 \text{ <}\text{< } n$。

### 思路 1：代码

```python
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        ans = float('inf')
        size = len(nums1)
        states = 1 << size

        dp = [float('inf') for _ in range(states)]
        dp[0] = 0
        for state in range(states):
            one_cnt = bin(state).count('1')
            for i in range(size):
                if (state >> i) & 1:
                    dp[state] = min(dp[state], dp[state ^ (1 << i)] + (nums1[i] ^ nums2[one_cnt - 1]))
        
        return dp[states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n \times n)$，其中 $n$ 是数组 $nums1$、$nums2$ 的长度。
- **空间复杂度**：$O(2^n)$。

