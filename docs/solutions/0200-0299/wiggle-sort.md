# [0280. 摆动排序](https://leetcode.cn/problems/wiggle-sort/)

- 标签：贪心、数组、排序
- 难度：中等

## 题目链接

- [0280. 摆动排序 - 力扣](https://leetcode.cn/problems/wiggle-sort/)

## 题目大意

**描述**：

给定一个的整数数组 $nums$。

**要求**：

将该数组重新排序后使 $nums[0] \le nums[1] \ge nums[2] \le nums[3]...$。

输入数组总是有一个有效的答案。

**说明**：

- $1 \le nums.length \le 5 \times 10^{4}$。
- $0 \le nums[i] \le 10^{4}$。
- 输入的 $nums$ 保证至少有一个答案。

 

- 进阶：你能在 $O(n)$ 时间复杂度下解决这个问题吗？

**示例**：

- 示例 1：

```python
输入：nums = [3,5,2,1,6,4]
输出：[3,5,1,6,2,4]
解释：[1,6,2,5,3,4]也是有效的答案
```

- 示例 2：

```python
输入：nums = [6,6,5,6,3,8]
输出：[6,6,5,6,3,8]
```

## 解题思路

### 思路 1：贪心算法

这是一个贪心算法问题。我们需要将数组重新排序，使得满足摆动条件：$nums[0] \le nums[1] \ge nums[2] \le nums[3]...$

核心思想是：
- 对于奇数位置 $i$（$i$ 为奇数），我们需要 $nums[i] \ge nums[i-1]$ 且 $nums[i] \ge nums[i+1]$（如果存在）
- 对于偶数位置 $i$（$i$ 为偶数），我们需要 $nums[i] \le nums[i-1]$ 且 $nums[i] \le nums[i+1]$（如果存在）

贪心策略：
- 遍历数组，对于每个位置 $i$，检查是否满足摆动条件
- 如果不满足，则与相邻元素交换，使得满足条件
- 具体来说：
  - 如果 $i$ 是奇数且 $nums[i] < nums[i-1]$，则交换 $nums[i]$ 和 $nums[i-1]$
  - 如果 $i$ 是偶数且 $nums[i] > nums[i-1]$，则交换 $nums[i]$ 和 $nums[i-1]$

### 思路 1：代码

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 遍历数组，确保每个位置都满足摆动条件
        for i in range(1, n):
            # 如果当前位置是奇数索引，需要 nums[i] >= nums[i-1]
            if i % 2 == 1:
                if nums[i] < nums[i-1]:
                    # 交换元素，使得 nums[i] >= nums[i-1]
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            # 如果当前位置是偶数索引，需要 nums[i] <= nums[i-1]
            else:
                if nums[i] > nums[i-1]:
                    # 交换元素，使得 nums[i] <= nums[i-1]
                    nums[i], nums[i-1] = nums[i-1], nums[i]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。只需要遍历一次数组，每个元素最多交换一次。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
