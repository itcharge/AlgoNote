# [0594. 最长和谐子序列](https://leetcode.cn/problems/longest-harmonious-subsequence/)

- 标签：数组、哈希表、计数、排序、滑动窗口
- 难度：简单

## 题目链接

- [0594. 最长和谐子序列 - 力扣](https://leetcode.cn/problems/longest-harmonious-subsequence/)

## 题目大意

**描述**：

和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是 1。

给定一个整数数组 $nums$。

**要求**：

在所有可能的「子序列」中找到最长的和谐子序列的长度。

**说明**：

- 数组的「子序列」是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
- $1 \le nums.length \le 2 * 10^{4}$。
- $-10^{9} \le nums[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长和谐子序列是 [3,2,2,2,3]。
```

- 示例 2：

```python
输入：nums = [1,2,3,4]
输出：2
解释：最长和谐子序列是 [1,2]，[2,3] 和 [3,4]，长度都为 2。
```

## 解题思路

### 思路 1：哈希表统计

和谐子序列要求最大值和最小值的差正好为 1，这意味着和谐子序列中只能包含两种不同的数字，且这两个数字相差 1。

我们可以使用哈希表统计每个数字出现的次数 $count[x]$。对于每个数字 $x$，如果存在 $x+1$，那么由 $x$ 和 $x+1$ 组成的和谐子序列长度为 $count[x] + count[x+1]$。

遍历所有数字，对于每个数字 $x$，计算 $count[x] + count[x+1]$（如果 $x+1$ 存在），取最大值即可。

### 思路 1：代码

```python
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 统计每个数字出现的次数
        count = Counter(nums)
        
        max_length = 0
        # 遍历所有数字
        for num in count:
            # 如果存在 num + 1，计算和谐子序列长度
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
        
        return max_length
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。需要遍历数组统计频率，然后遍历哈希表。
- **空间复杂度**：$O(n)$，哈希表最多存储 $n$ 个不同的数字。
