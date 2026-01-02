# [0697. 数组的度](https://leetcode.cn/problems/degree-of-an-array/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [0697. 数组的度 - 力扣](https://leetcode.cn/problems/degree-of-an-array/)

## 题目大意

**描述**：

给定一个非空且只包含非负数的整数数组 $nums$，数组的「度」的定义是指数组里任一元素出现频数的最大值。

**要求**：

在 $nums$ 中找到与 $nums$ 拥有相同大小的度的最短连续子数组，返回其长度。

**说明**：

- $nums.length$ 在 $1$ 到 $50,000$ 范围内。
- $nums[i]$ 是一个在 $0$ 到 $49,999$ 范围内的整数。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,2,3,1]
输出：2
解释：
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。
```

- 示例 2：

```python
输入：nums = [1,2,2,3,1,4,2]
输出：6
解释：
数组的度是 3 ，因为元素 2 重复出现 3 次。
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。
```

## 解题思路

### 思路 1：哈希表

#### 思路 1：算法描述

这道题目要求找到与原数组拥有相同度的最短连续子数组。数组的度定义为数组里任一元素出现频数的最大值。

我们可以使用哈希表来记录每个元素的出现次数、第一次出现的位置和最后一次出现的位置。

具体步骤如下：

1. 初始化三个哈希表：
   - $count$：记录每个元素的出现次数。
   - $first$：记录每个元素第一次出现的位置。
   - $last$：记录每个元素最后一次出现的位置。
2. 遍历数组 $nums$，更新三个哈希表。
3. 找到数组的度 $degree$，即 $count$ 中的最大值。
4. 遍历 $count$，找到所有出现次数等于 $degree$ 的元素，计算它们对应的子数组长度 $last[num] - first[num] + 1$，取最小值。
5. 返回最小值。

#### 思路 1：代码

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}   # 记录每个元素的出现次数
        first = {}   # 记录每个元素第一次出现的位置
        last = {}    # 记录每个元素最后一次出现的位置
        
        # 遍历数组，更新哈希表
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 1
                first[num] = i
            else:
                count[num] += 1
            last[num] = i
        
        # 找到数组的度
        degree = max(count.values())
        
        # 找到最短子数组长度
        min_len = len(nums)
        for num, cnt in count.items():
            if cnt == degree:
                min_len = min(min_len, last[num] - first[num] + 1)
        
        return min_len
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。需要遍历两次数组。
- **空间复杂度**：$O(n)$。需要使用三个哈希表存储信息。
