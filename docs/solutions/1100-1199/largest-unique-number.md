# [1133. 最大唯一数](https://leetcode.cn/problems/largest-unique-number/)

- 标签：数组、哈希表、排序
- 难度：简单

## 题目链接

- [1133. 最大唯一数 - 力扣](https://leetcode.cn/problems/largest-unique-number/)

## 题目大意

**描述**：给定一个整数数组 $A$。

**要求**：找出数组中只出现一次的最大整数。如果没有这样的整数，返回 $-1$。

**说明**：

- $1 \le A.length \le 2000$。
- $0 \le A[i] \le 10^{3}$。

**示例**：

```python
输入：[5,7,3,9,4,9,8,3,1]
输出：8
解释：9 出现了两次，8 只出现一次且最大，所以答案是 8。
```

## 解题思路

### 思路 1：哈希表 + 排序

先用哈希表统计每个数字出现的次数，然后从大到小找第一个只出现一次的数字。

**步骤拆解：**

1. 遍历数组，用字典记下每个数字出现的次数。
2. 把数组从大到小排序。
3. 遍历排好序的数组，找到第一个出现次数为 1 的数字，返回它。
4. 如果全部都有重复，返回 $-1$。

### 思路 1：代码

```python
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # 统计每个数字出现了几次
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # 从大到小排序
        nums.sort(reverse=True)
        for num in nums:
            if count_map[num] == 1:  # 只出现一次
                return num
        
        return -1  # 没有唯一的数
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$。排序花的时间最多。
- **空间复杂度**：$O(n)$。哈希表需要存每个数字的计数。
