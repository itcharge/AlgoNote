# [0334. 递增的三元子序列](https://leetcode.cn/problems/increasing-triplet-subsequence/)

- 标签：贪心、数组
- 难度：中等

## 题目链接

- [0334. 递增的三元子序列 - 力扣](https://leetcode.cn/problems/increasing-triplet-subsequence/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：判断数组中是否存在长度为 3 的递增子序列。

**说明**：

- 要求算法时间复杂度为 $O(n)$、空间复杂度为 $O(1)$。
- **长度为 $3$ 的递增子序列**：存在这样的三元组下标 ($i$, $j$, $k$) 且满足 $i < j < k$ ，使得 $nums[i] < nums[j] < nums[k]$。
- $1 \le nums.length \le 5 \times 10^5$。
- $-2^{31} \le nums[i] \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
```

- 示例 2：

```python
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
```

## 解题思路

### 思路 1：快慢指针

常规方法是三重 `for` 循环遍历三个数，但是时间复杂度为 $O(n^3)$，肯定会超时的。

那么如何才能只进行一次遍历，就找到长度为 3 的递增子序列呢？

假设长度为 3 的递增子序列元素为 $a$、$b$、$c$，$a < b < c$。

先来考虑 $a$ 和 $b$。如果我们要使得一个数组  $i < j$，并且 $nums[i] < nums[j]$。那么应该使得 $a$ 尽可能的小，这样子我们下一个数字 $b$ 才可以尽可能地满足条件。

同样对于 $b$ 和 $c$，也应该使得 $b$ 尽可能的小，下一个数字 $c$ 才可以尽可能的满足条件。

所以，我们的目的是：在 $a < b$ 的前提下，保证 a 尽可能小。在 $b < c$ 的条件下，保证 $b$ 尽可能小。

我们可以使用两个数 $a$、$b$ 指向无穷大。遍历数组：

- 如果当前数字小于等于 $a$ ，则更新 `a = num`；
- 如果当前数字大于等于 $a$，则说明当前数满足 $num > a$，则判断：
  - 如果 $num \le b$，则更新 `b = num`；
  - 如果 $num > b$，则说明找到了长度为 3 的递增子序列，直接输出 $True$。
- 如果遍历完仍未找到，则输出 $False$。

### 思路 1：代码

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

