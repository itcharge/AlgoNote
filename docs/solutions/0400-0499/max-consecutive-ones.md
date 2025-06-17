# [0485. 最大连续 1 的个数](https://leetcode.cn/problems/max-consecutive-ones/)

- 标签：数组
- 难度：简单

## 题目链接

- [0485. 最大连续 1 的个数 - 力扣](https://leetcode.cn/problems/max-consecutive-ones/)

## 题目大意

**描述**：给定一个二进制数组 $nums$， 数组中只包含 $0$ 和 $1$。

**要求**：计算其中最大连续 $1$ 的个数。

**说明**：

- $1 \le nums.length \le 10^5$。
- $nums[i]$ 不是 $0$ 就是 $1$。

**示例**：

- 示例 1：

```python
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
```

- 示例 2：

```python
输入：nums = [1,0,1,1,0,1]
输出：2
```

## 解题思路

### 思路 1：一次遍历

1. 使用两个变量 $cnt$ 和 $ans$。$cnt$ 用于存储当前连续 $1$ 的个数，$ans$ 用于存储最大连续 $1$ 的个数。
2. 然后进行一次遍历，统计当前连续 $1$ 的个数，并更新最大的连续 $1$ 个数。
3. 最后返回 $ans$ 作为答案。

### 思路 1：代码

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

