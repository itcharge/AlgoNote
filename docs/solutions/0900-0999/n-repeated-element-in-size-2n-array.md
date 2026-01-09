# [0961. 在长度 2N 的数组中找出重复 N 次的元素](https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [0961. 在长度 2N 的数组中找出重复 N 次的元素 - 力扣](https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/)

## 题目大意

**描述**：

给定一个整数数组 $nums$，该数组具有以下属性：

- $nums.length == 2 \times n$。
- $nums$ 包含 $n + 1$ 个「不同的」元素。
- $nums$ 中恰有一个元素重复 $n$ 次。

**要求**：

找出并返回重复了 $n$ 次的那个元素。

**说明**：

- $2 \le n \le 5000$。
- $nums.length == 2 \times n$。
- $0 \le nums[i] \le 10^{4}$。
- $nums$ 由 $n + 1$ 个「不同的」元素组成，且其中一个元素恰好重复 $n$ 次。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,3]
输出：3
```

- 示例 2：

```python
输入：nums = [2,1,2,5,3,2]
输出：2
```

## 解题思路

### 思路 1：哈希表

由于数组长度为 $2 \times n$，包含 $n+1$ 个不同元素，且恰有一个元素重复 $n$ 次，所以只需要找到出现次数最多的元素即可。

1. **使用哈希表**：遍历数组，统计每个元素的出现次数。
2. **返回结果**：返回出现次数为 $n$ 的元素。

**优化**：由于重复元素占据了一半的位置，我们可以使用更简单的方法：只要发现某个元素出现第二次，就返回它。

### 思路 1：代码

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度，最多遍历一次数组。
- **空间复杂度**：$O(n)$，需要使用哈希集合存储已访问的元素。
