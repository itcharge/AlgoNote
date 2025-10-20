# [0229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii/)

- 标签：数组、哈希表、计数、排序
- 难度：中等

## 题目链接

- [0229. 多数元素 II - 力扣](https://leetcode.cn/problems/majority-element-ii/)

## 题目大意

**描述**：

给定一个大小为 $n$ 的整数数组。

**要求**：

找出其中所有出现超过 $\lfloor n/3 \rfloor$ 次的元素。

**说明**：

- $1 \le nums.length \le 5 \times 10^{4}$。
- $-10^{9} \le nums[i] \le 10^{9}$。

- 进阶：尝试设计时间复杂度为 $O(n)$、空间复杂度为 $O(1)$ 的算法解决此问题。

**示例**：

- 示例 1：

```python
示例 1：


输入：nums = [3,2,3]
输出：[3]
```

- 示例 2：

```python
输入：nums = [1]
输出：[1]
```

## 解题思路

### 思路 1：哈希表计数

这是一个经典的多数元素问题。我们需要找出所有出现次数超过 $\lfloor n/3 \rfloor$ 次的元素。

核心思想是：

- 使用哈希表统计每个元素 $nums[i]$ 的出现次数 $count$。
- 遍历数组，对每个元素进行计数：$count[nums[i]] += 1$。
- 遍历哈希表，找出所有满足 $count[element] > \lfloor n/3 \rfloor$ 的元素。

具体算法步骤：

1. 初始化哈希表 $count = \{\}$ 和结果列表 $result = []$。
2. 遍历数组 $nums$，统计每个元素的出现次数。
3. 计算阈值 $threshold = \lfloor len(nums) / 3 \rfloor$。
4. 遍历哈希表，找出所有出现次数大于阈值的元素。
5. 返回结果列表。

### 思路 1：代码

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 使用哈希表统计每个元素的出现次数
        count = {}
        
        # 遍历数组，统计每个元素的出现次数
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # 计算阈值：出现次数需要超过 ⌊n/3⌋
        threshold = len(nums) // 3
        
        # 找出所有出现次数超过阈值的元素
        result = []
        for num, freq in count.items():
            if freq > threshold:
                result.append(num)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。需要遍历数组一次进行计数，然后遍历哈希表一次找出结果。
- **空间复杂度**：$O(n)$，最坏情况下哈希表需要存储所有不同的元素。
