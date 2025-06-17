# [0704. 二分查找](https://leetcode.cn/problems/binary-search/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [0704. 二分查找 - 力扣](https://leetcode.cn/problems/binary-search/)

## 题目大意

**描述**：给定一个升序的数组 $nums$，和一个目标值 $target$。

**要求**：返回 $target$ 在数组中的位置，如果找不到，则返回 -1。

**说明**：

- 你可以假设 $nums$ 中的所有元素是不重复的。
- $n$ 将在 $[1, 10000]$之间。
- $nums$ 的每个元素都将在 $[-9999, 9999]$之间。

**示例**：

- 示例 1：

```python
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

- 示例 2：

```python
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

## 解题思路

### 思路 1：二分查找

设定左右节点为数组两端，即 `left = 0`，`right = len(nums) - 1`，代表待查找区间为 $[left, right]$（左闭右闭）。

取两个节点中心位置 $mid$，先比较中心位置值 $nums[mid]$ 与目标值 $target$ 的大小。

- 如果 $target == nums[mid]$，则返回中心位置。
- 如果 $target > nums[mid]$，则将左节点设置为 $mid + 1$，然后继续在右区间 $[mid + 1, right]$ 搜索。
- 如果中心位置值 $target < nums[mid]$，则将右节点设置为 $mid - 1$，然后继续在左区间 $[left, mid - 1]$ 搜索。

### 思路 1：代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # 在区间 [left, right] 内查找 target
        while left <= right:
            # 取区间中间节点
            mid = (left + right) // 2
            # 如果找到目标值，则直接返回中心位置
            if nums[mid] == target:
                return mid
            # 如果 nums[mid] 小于目标值，则在 [mid + 1, right] 中继续搜索
            elif nums[mid] < target:
                left = mid + 1
            # 如果 nums[mid] 大于目标值，则在 [left, mid - 1] 中继续搜索
            else:
                right = mid - 1
        # 未搜索到元素，返回 -1
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$。

