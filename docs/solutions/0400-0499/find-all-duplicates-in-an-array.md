# [0442. 数组中重复的数据](https://leetcode.cn/problems/find-all-duplicates-in-an-array/)

- 标签：数组、哈希表
- 难度：中等

## 题目链接

- [0442. 数组中重复的数据 - 力扣](https://leetcode.cn/problems/find-all-duplicates-in-an-array/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的整数数组 $nums$，其中 $nums$ 的所有整数都在范围 $[1, n]$ 内，且每个整数出现「最多两次」。

**要求**：

请你找出所有出现「两次」的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 $O(n)$ 且仅使用常量额外空间（不包括存储输出所需的空间）的算法解决此问题。

**说明**：

- $n == nums.length$。
- $1 \le n \le 10^{5}$。
- $1 \le nums[i] \le n$。
- $nums$ 中的每个元素出现「一次」或「两次」。

**示例**：

- 示例 1：

```python
输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]
```

- 示例 2：

```python
输入：nums = [1,1,2]
输出：[1]
```

## 解题思路

### 思路 1：正负号标记法

由于数组中的元素都在范围 $[1, n]$ 内，且每个整数最多出现两次。可以利用数组中的位置索引本身来表示数字是否存在。

我们可以遍历数组 $nums$，对于每一个元素 $nums[i]$：
- 如果 $nums[abs(nums[i]) - 1] > 0$，说明 $abs(nums[i])$ 第一次出现，将其对应位置的数变为负数作为标记。
- 如果 $nums[abs(nums[i]) - 1] < 0$，说明 $abs(nums[i])$ 已经出现过一次了，此时 $abs(nums[i])$ 就是重复的数字，将其加入到结果数组中。

算法步骤如下：
- 初始化结果数组 $res$。
- 遍历数组 $nums$，对于每个元素 $nums[i]$：
  - 计算 $abs(nums[i]) - 1$ 作为索引 $index$。
  - 如果 $nums[index] < 0$，说明 $abs(nums[i])$ 是重复数字，将其加入 $res$。
  - 否则将 $nums[index]$ 标记为负数，即 $nums[index] = -nums[index]$。
- 遍历结束后，返回结果数组 $res$。

### 思路 1：代码

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        # 遍历数组，使用正负号标记法
        for i in range(len(nums)):
            # 计算索引位置
            index = abs(nums[i]) - 1
            
            # 如果该位置的数已经是负数，说明已经出现过一次
            if nums[index] < 0:
                # 将当前元素（取绝对值）加入结果数组
                res.append(abs(nums[i]))
            else:
                # 将该位置的数标记为负数
                nums[index] = -nums[index]
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组长度。我们只需要遍历一次数组。
- **空间复杂度**：$O(1)$。除了返回结果数组，只使用了常数额外空间。
