# [2172. 数组的最大与和](https://leetcode.cn/problems/maximum-and-sum-of-array/)

- 标签：位运算、数组、动态规划、状态压缩
- 难度：困难

## 题目链接

- [2172. 数组的最大与和 - 力扣](https://leetcode.cn/problems/maximum-and-sum-of-array/)

## 题目大意

**描述**：给定一个长度为 $n$ 的整数数组 $nums$ 和一个整数 $numSlots$ 满足 $2 \times numSlots \ge n$。一共有 $numSlots$ 个篮子，编号为 $1 \sim numSlots$。

现在需要将所有 $n$ 个整数分到这些篮子中，且每个篮子最多有 $2$ 个整数。

**要求**：返回将 $nums$ 中所有数放入 $numSlots$ 个篮子中的最大与和。

**说明**：

- **与和**：当前方案中，每个数与它所在篮子编号的按位与运算结果之和。
  - 比如，将数字 $[1, 3]$ 放入篮子 $1$ 中，$[4, 6]$ 放入篮子 $2$ 中，这个方案的与和为 $(1 \text{ AND } 1) + (3 \text{ AND } 1) + (4 \text{ AND } 2) + (6 \text{ AND } 2) = 1 + 1 + 0 + 2 = 4$。
- $n == nums.length$。
- $1 \le numSlots \le 9$。
- $1 \le n \le 2 \times numSlots$。
- $1 \le nums[i] \le 15$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,4,5,6], numSlots = 3
输出：9
解释：一个可行的方案是 [1, 4] 放入篮子 1 中，[2, 6] 放入篮子 2 中，[3, 5] 放入篮子 3 中。
最大与和为 (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 1 + 0 + 2 + 2 + 3 + 1 = 9。
```

- 示例 2：

```python
输入：nums = [1,3,10,4,7,1], numSlots = 9
输出：24
解释：一个可行的方案是 [1, 1] 放入篮子 1 中，[3] 放入篮子 3 中，[4] 放入篮子 4 中，[7] 放入篮子 7 中，[10] 放入篮子 9 中。
最大与和为 (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + (10 AND 9) = 1 + 1 + 3 + 4 + 7 + 8 = 24 。
注意，篮子 2 ，5 ，6 和 8 是空的，这是允许的。
```

## 解题思路

### 思路 1：状压 DP

每个篮子最多可分 $2$ 个整数，则我们可以将 $1$ 个篮子分成两个篮子，这样总共有 $2 \times numSlots$ 个篮子，每个篮子中最多可以装 $1$ 个整数。

同时因为 $numSlots$ 的范围为 $[1, 9]$，$2 \times numSlots$ 的范围为 $[2, 19]$，范围不是很大，所以我们可以用「状态压缩」的方式来表示每个篮子中的整数放取情况。

即使用一个 $n \times numSlots$ 位的二进制数 $state$ 来表示每个篮子中的整数放取情况。如果 $state$ 的第 $i$ 位为 $1$，表示第 $i$ 个篮子里边放了整数，如果 $state$ 的第 $i$ 位为 $0$，表示第 $i$ 个篮子为空。

这样，我们就可以通过动态规划的方式来解决这道题。

###### 1. 划分阶段

按照 $2 \times numSlots$ 个篮子中的整数放取情况进行阶段划分。

###### 2. 定义状态

定义当前每个篮子中的整数放取情况为 $state$，$state$ 对应选择的整数个数为 $count(state)$。

则可以定义状态 $dp[state]$ 表示为：将前 $count(state)$ 个整数放到篮子里，并且每个篮子中的整数放取情况为 $state$ 时，可以获得的最大与和。

###### 3. 状态转移方程

对于当前状态 $dp[state]$，肯定是从比 $state$ 少选一个元素的状态中递推而来。我们可以枚举少选一个元素的状态，找到可以获得的最大与和，赋值给 $dp[state]$。

即状态转移方程为：$dp[state] = min(dp[state], dp[state \oplus (1 \text{ <}\text{< } i)] + (i // 2 + 1) \text{ \& } nums[one\_cnt - 1])$，其中：

1. $state$ 第 $i$ 位一定为 $1$。
2. $state \oplus (1 \text{ <}\text{< } i)$ 为比 $state$ 少选一个元素的状态。
3. $i // 2 + 1$ 为篮子对应编号
4. $nums[one\_cnt - 1]$ 为当前正在考虑的数组元素。

###### 4. 初始条件

- 初始每个篮子中都没有放整数的情况下，可以获得的最大与和为 $0$，即 $dp[0] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[state]$ 表示为：将前 $count(state)$ 个整数放到篮子里，并且每个篮子中的整数放取情况为 $state$ 时，可以获得的最大与和。所以最终结果为 $max(dp)$。

> 注意：当 $one\_cnt > len(nums)$ 时，无法通过递推得到 $dp[state]$，需要跳过。

### 思路 1：代码

```python
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        states = 1 << (numSlots * 2)
        dp = [0 for _ in range(states)]

        for state in range(states):
            one_cnt = bin(state).count('1')
            if one_cnt > len(nums):
                continue
            for i in range(numSlots * 2):
                if (state >> i) & 1:
                    dp[state] = max(dp[state], dp[state ^ (1 << i)] + ((i // 2 + 1) & nums[one_cnt - 1]))
        
        return max(dp)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^m \times m)$，其中 $m = 2 \times numSlots$。
- **空间复杂度**：$O(2^m)$。

