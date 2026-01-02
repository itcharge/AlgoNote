# [0645. 错误的集合](https://leetcode.cn/problems/set-mismatch/)

- 标签：位运算、数组、哈希表、排序
- 难度：简单

## 题目链接

- [0645. 错误的集合 - 力扣](https://leetcode.cn/problems/set-mismatch/)

## 题目大意

**描述**：

集合 $s$ 包含从 $1$ 到 $n$ 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合「丢失了一个数字」并且「有一个数字重复」。

给定一个数组 $nums$ 代表了集合 $S$ 发生错误后的结果。

**要求**：

找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

**说明**：

- $2 \le nums.length \le 10^{4}$。
- $1 \le nums[i] \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,2,4]
输出：[2,3]
```

- 示例 2：

```python
输入：nums = [1,1]
输出：[1,2]
```

## 解题思路

### 思路 1：哈希表

这道题目要求找出重复的数字和丢失的数字。可以使用哈希表记录每个数字出现的次数。

1. 使用哈希表 $freq$ 记录数组中每个数字出现的次数。
2. 遍历 $1$ 到 $n$：
   - 如果 $freq[i] = 2$，说明 $i$ 是重复的数字。
   - 如果 $freq[i] = 0$，说明 $i$ 是丢失的数字。
3. 返回 `[重复的数字, 丢失的数字]`。

### 思路 1：代码

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        n = len(nums)
        freq = Counter(nums)
        duplicate, missing = 0, 0
        
        for i in range(1, n + 1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i
        
        return [duplicate, missing]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。需要遍历数组一次统计频率，再遍历 $1$ 到 $n$ 找出重复和丢失的数字。
- **空间复杂度**：$O(n)$，需要使用哈希表存储每个数字的频率。

### 思路 2：数学方法

利用数学方法，通过求和和平方和来找出重复和丢失的数字。

1. 设重复的数字为 $x$，丢失的数字为 $y$。
2. 计算数组的和 $sum\underline{~}nums$ 和 $1$ 到 $n$ 的和 $sum\underline{~}n$，有：$sum\underline{~}nums - sum\underline{~}n = x - y$。
3. 计算数组的平方和 $sum\underline{~}sq\underline{~}nums$ 和 $1$ 到 $n$ 的平方和 $sum\underline{~}sq\underline{~}n$，有：$sum\underline{~}sq\underline{~}nums - sum\underline{~}sq\underline{~}n = x^2 - y^2 = (x + y)(x - y)$。
4. 通过这两个方程可以求出 $x$ 和 $y$。

### 思路 2：代码

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 计算数组的和与平方和
        sum_nums = sum(nums)
        sum_sq_nums = sum(x * x for x in nums)
        
        # 计算 1 到 n 的和与平方和
        sum_n = n * (n + 1) // 2
        sum_sq_n = n * (n + 1) * (2 * n + 1) // 6
        
        # x - y = sum_nums - sum_n
        diff = sum_nums - sum_n
        
        # x^2 - y^2 = sum_sq_nums - sum_sq_n
        # (x + y)(x - y) = sum_sq_nums - sum_sq_n
        # x + y = (sum_sq_nums - sum_sq_n) / (x - y)
        sum_xy = (sum_sq_nums - sum_sq_n) // diff
        
        # 求解 x 和 y
        duplicate = (diff + sum_xy) // 2
        missing = sum_xy - duplicate
        
        return [duplicate, missing]
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。需要遍历数组计算和与平方和。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
